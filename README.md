# linux
1 основные принципы Unix-way:
-одна задача - одна программа 
-все есть файл
-есть множество путей решения 
2 Линус Торвальдс является разработчиком чего
- Создатель ядра Linux и системы управления версиями Git
3 Как посмыотреть название ядра системы из консоли?
- команда uname
4 Промежутки измерения загрузки системы для команды uptime следующие
- 1, 5 и 15 минут 
5 какой командой узнать сколько занято на HDD
- df -H
6 какие разделы содержит вывод команды vmstat
-Procs – r: Общее количество процессов, ожидающих запуска.
-Procs – b: Общее количество занятых процессов.
-Memory – swpd: Использованная виртуальная память.
-Memory – free: Свободная виртуальная память.
-Memory – buff: Память используемая в качестве буфера.
-Memory – cache:Память используемая в качестве кэша.
-Swap – si: Память которая использует СВАП (swapped) с диска (за каждую секунду).
-Swap – so:Память которая использует СВАП (swapped) на диск (за каждую секунду).
-IO – bi: Блоки «in». Т.е. блоки, посылаемые от устройства (за каждую секунду).
-IO – bo: Блоки «out». Блоки, посылаемые на устройство (за каждую секунду).
-System – in:  Количество прерываний в секунду.
-System – cs: Переключение контекста.
-CPU – us, sy, id, wa, st: Процессорное время пользователя ( CPU user time), Системное время (system time), время простоя (idle time), время ожидания (wait time).

7 Описать работу своего Linux дистрибутива: какое ядро, архитектура, размеры hdd, объеме ОЗУ, загрузке процессора и т.д.
 uname -a
 Linux baldini-virtual-machine 5.13.0-28-generic #31~20.04.1-Ubuntu SMP Wed Jan 19 14:08:10 UTC 2022 x86_64 x86_64 x86_64 GNU/Linux
5.13.0-28-generic версия ядра
SMP — ядро Linux поддерживает многоядерные и многопроцессорные системы
x86_64 — говорит о том, что система x64 битная
df -H

Filesystem      Size  Used Avail Use% Mounted on
udev            1.5G     0  1.5G   0% /dev
tmpfs           302M  1.9M  300M   1% /run
/dev/sda5        53G   35G   16G  69% /
tmpfs           1.6G     0  1.6G   0% /dev/shm
tmpfs           5.3M  4.1k  5.3M   1% /run/lock
tmpfs           1.6G     0  1.6G   0% /sys/fs/cgroup
/dev/loop0      132k  132k     0 100% /snap/bare/5
/dev/loop2      116M  116M     0 100% /snap/core/12603
/dev/loop1      105M  105M     0 100% /snap/core/11993
/dev/loop3       59M   59M     0 100% /snap/core18/2284
/dev/loop4       66M   66M     0 100% /snap/core20/1328
/dev/loop5      514M  514M     0 100% /snap/datagrip/129
/dev/loop6      261M  261M     0 100% /snap/gnome-3-38-2004/99
/dev/loop7      2.1M  2.1M     0 100% /snap/serve/170
/dev/loop8      261M  261M     0 100% /snap/gnome-3-38-2004/87
/dev/loop9       69M   69M     0 100% /snap/gtk-common-themes/1515
/dev/loop10      57M   57M     0 100% /snap/snap-store/558
/dev/loop11     230M  230M     0 100% /snap/gnome-3-34-1804/72
/dev/loop12      69M   69M     0 100% /snap/gtk-common-themes/1519
/dev/loop13      66M   66M     0 100% /snap/core20/1270
/dev/loop14     311M  311M     0 100% /snap/vlc/2344
/dev/loop15     6.6M  6.6M     0 100% /snap/curl/484
/dev/loop16     514M  514M     0 100% /snap/datagrip/128
/dev/loop17     230M  230M     0 100% /snap/gnome-3-34-1804/77
/dev/loop18     177M  177M     0 100% /snap/postman/149
/dev/loop19     564M  564M     0 100% /snap/webstorm/243
/dev/loop20     564M  564M     0 100% /snap/webstorm/239
/dev/loop21     340M  340M     0 100% /snap/telegram-desktop/3530
/dev/loop22     6.7M  6.7M     0 100% /snap/curl/623
/dev/loop23     340M  340M     0 100% /snap/telegram-desktop/3544
/dev/loop24     177M  177M     0 100% /snap/postman/148
/dev/loop25      54M   54M     0 100% /snap/snap-store/547
/dev/loop26      59M   59M     0 100% /snap/core18/2253
/dev/sda1       536M  4.1k  536M   1% /boot/efi
tmpfs           302M   29k  302M   1% /run/user/1000
/dev/loop29      46M   46M     0 100% /snap/snapd/14978

ОЗУ 
free -h
             total        used        free      shared  buff/cache   available
Mem:          2.8Gi       1.3Gi       206Mi       3.0Mi       1.3Gi       1.4Gi
Swap:         1.3Gi       1.0Mi       1.3Gi

Загрузка процессора
uptime
20:34:19 up 11 min,  1 user,  load average: 0.41, 0.26, 0.22
