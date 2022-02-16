# linux lab1 Балдин И.А.
1) основные принципы Unix-way: <br />
-одна задача - одна программа  <br />
-все есть файл <br />
-есть множество путей решения  <br />
2) Линус Торвальдс является разработчиком чего <br />
- Создатель ядра Linux и системы управления версиями Git <br />
3) Как посмыотреть название ядра системы из консоли? <br />
- команда uname <br />
4) Промежутки измерения загрузки системы для команды uptime следующие <br />
- 1, 5 и 15 минут  <br />
5) какой командой узнать сколько занято на HDD <br />
- df -H <br />
6) какие разделы содержит вывод команды vmstat <br />
-Procs – r: Общее количество процессов, ожидающих запуска. <br />
-Procs – b: Общее количество занятых процессов. <br />
-Memory – swpd: Использованная виртуальная память. <br />
-Memory – free: Свободная виртуальная память. <br />
-Memory – buff: Память используемая в качестве буфера. <br />
-Memory – cache:Память используемая в качестве кэша. <br />
-Swap – si: Память которая использует СВАП (swapped) с диска (за каждую секунду). <br />
-Swap – so:Память которая использует СВАП (swapped) на диск (за каждую секунду). <br />
-IO – bi: Блоки «in». Т.е. блоки, посылаемые от устройства (за каждую секунду). <br />
-IO – bo: Блоки «out». Блоки, посылаемые на устройство (за каждую секунду). <br />
-System – in:  Количество прерываний в секунду. <br />
-System – cs: Переключение контекста. <br />
-CPU – us, sy, id, wa, st: Процессорное время пользователя ( CPU user time), Системное время (system time), время простоя (idle time), время ожидания (wait time). <br />

7) Описать работу своего Linux дистрибутива: какое ядро, архитектура, размеры hdd, объеме ОЗУ, загрузке процессора и т.д. <br />
 uname -a <br />
 Linux baldini-virtual-machine 5.13.0-28-generic #31~20.04.1-Ubuntu SMP Wed Jan 19 14:08:10 UTC 2022 x86_64 x86_64 x86_64 GNU/Linux <br />
5.13.0-28-generic версия ядра <br />
SMP — ядро Linux поддерживает многоядерные и многопроцессорные системы <br />
x86_64 — говорит о том, что система x64 битная <br />
Размер hdd
df -H <br />

Filesystem      Size  Used Avail Use% Mounted on <br />
udev            1.5G     0  1.5G   0% /dev <br />
tmpfs           302M  1.9M  300M   1% /run <br />
/dev/sda5        53G   35G   16G  69% / <br />
tmpfs           1.6G     0  1.6G   0% /dev/shm <br />
tmpfs           5.3M  4.1k  5.3M   1% /run/lock <br />
tmpfs           1.6G     0  1.6G   0% /sys/fs/cgroup <br />
/dev/loop0      132k  132k     0 100% /snap/bare/5 <br />
/dev/loop2      116M  116M     0 100% /snap/core/12603 <br />
/dev/loop1      105M  105M     0 100% /snap/core/11993 <br />
/dev/loop3       59M   59M     0 100% /snap/core18/2284 <br />
/dev/loop4       66M   66M     0 100% /snap/core20/1328 <br />
/dev/loop5      514M  514M     0 100% /snap/datagrip/129 <br />
/dev/loop6      261M  261M     0 100% /snap/gnome-3-38-2004/99 <br />
/dev/loop7      2.1M  2.1M     0 100% /snap/serve/170 <br />
/dev/loop8      261M  261M     0 100% /snap/gnome-3-38-2004/87 <br />
/dev/loop9       69M   69M     0 100% /snap/gtk-common-themes/1515 <br />
/dev/loop10      57M   57M     0 100% /snap/snap-store/558 <br />
/dev/loop11     230M  230M     0 100% /snap/gnome-3-34-1804/72 <br />
/dev/loop12      69M   69M     0 100% /snap/gtk-common-themes/1519 <br />
/dev/loop13      66M   66M     0 100% /snap/core20/1270 <br />
/dev/loop14     311M  311M     0 100% /snap/vlc/2344 <br />
/dev/loop15     6.6M  6.6M     0 100% /snap/curl/484 <br />
/dev/loop16     514M  514M     0 100% /snap/datagrip/128 <br />
/dev/loop17     230M  230M     0 100% /snap/gnome-3-34-1804/77 <br />
/dev/loop18     177M  177M     0 100% /snap/postman/149 <br />
/dev/loop19     564M  564M     0 100% /snap/webstorm/243 <br />
/dev/loop20     564M  564M     0 100% /snap/webstorm/239 <br />
/dev/loop21     340M  340M     0 100% /snap/telegram-desktop/3530 <br />
/dev/loop22     6.7M  6.7M     0 100% /snap/curl/623 <br />
/dev/loop23     340M  340M     0 100% /snap/telegram-desktop/3544 <br />
/dev/loop24     177M  177M     0 100% /snap/postman/148 <br />
/dev/loop25      54M   54M     0 100% /snap/snap-store/547 <br />
/dev/loop26      59M   59M     0 100% /snap/core18/2253 <br />
/dev/sda1       536M  4.1k  536M   1% /boot/efi <br />
tmpfs           302M   29k  302M   1% /run/user/1000 <br />
/dev/loop29      46M   46M     0 100% /snap/snapd/14978 <br />

ОЗУ  <br />
free -h <br />
             total        used        free      shared  buff/cache   available <br />
Mem:          2.8Gi       1.3Gi       206Mi       3.0Mi       1.3Gi       1.4Gi <br />
Swap:         1.3Gi       1.0Mi       1.3Gi <br />

Загрузка процессора <br />
uptime <br />
20:34:19 up 11 min,  1 user,  load average: 0.41, 0.26, 0.22
