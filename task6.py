import time
import psutil
import sys
import os

workers = []
GPID =os.getpid()
logFileName = './out.txt'

def main():
    message = sys.argv[sys.argv.index('-m')+1]
    process = int(sys.argv[sys.argv.index('-p')+1])
    iter = int(sys.argv[sys.argv.index('-i')+1])
    
    for i in range(process):
        print(f'P {os.getpid()}: Forking {i}')
        workerPid = os.fork()
        if not workerPid:
            now = time.time()
            for j in range(iter*(i+1)):
                with open(logFileName, mode='a+') as file:
                    file.write(f'C {i}: {message} {j+1}\n')
                time.sleep(1)
                if not psutil.pid_exists(GPID):
                    os.abort()
            os.abort()
        workers.append(workerPid)

    for pid in workers:
        print(f'P: Waiting for {pid}')
        done = os.waitpid(pid, 0)

if __name__ == "__main__":
    try:
        main() 
    except Exception:
        for i in workers:
            os.kill(i, 0)
