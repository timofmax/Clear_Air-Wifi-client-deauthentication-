# clean_air
clean air - pirate your Air*
**Automated launch of tools included in Kali**
airmon-ng, aireplay-ng

**How it's looks like?**
https://youtu.be/YG_E9oWFI04

**Tested on:**<br>
Python 3.6.2 <br>
Linux 4.9.0-kali3-amd64 #1 SMP Debian 4.9.18-1kali1 (2017-04-04) x86_64 GNU/Linux <br>
Wireless Adapter: Alfa AWUS036NH, chip RT2870/RT3070<br>
airmon-ng==Version 1.2-rc4<br>
aireplay-ng==Version 1.2-rc4<br>

**Idea:** 
Disconnects all clients from all AP, gives option don't disturb one AP *


Please use <a href="https://translate.google.com/?hl=ru#view=home&op=translate&sl=ru&tl=en&text=не%20мешай">GT</a> to read below instructrion :D <br>
**Текущая логика:**
1) Выбрать сетевой интерфейс, который надо перевести в режим мониторинга.
1.1 Проверяются, убиваются процессы мешающие запуску режима мониторинга.
2) Собирается инфа о всех AP по каналам 1-14, 2 ghz (время 5сек)
зависит от возможностей вашего чипа.
3) Выбрать # friendly BSSID (клиенты этой AP деавторизовываться не будут)
3.1 Посмотреть крутую анимацию. Можно кастомизировать в air_module.py
3.2 Список всех просканированных сетей выводятся в порядке #i ESSID BSSID #channel
4) Выбрать диапазон каналов работы.
5) Указать время работы скрипта (сек).
5) aireplay-ng последовательно обходит каждую AP BSSID в диапазоне. п.4*


**Код уныл, надо переписать! PEP! КОКОКО!<br>
Шли issue, пуль новое чё. Инициатива наказуема.**

**В планах:**
1) Предоставить возможность выбора времени, для п.2 логика
2) Предоставить возможность выбора времени, для п.5 логика по каждой AP
2) Убрать крутую анимацию, или заменить еще более крутой *Joke
3) Сделать log для AP по которым работал aireplay.
4) Прикрутить сортировку/работу с каждой AP по силе сигнала AP.
5) Ускорить процесс по работе на каждом канале, при условии отсутствия клиентов на AP.
6) Разобраться с кодировкой некоторых ESSID п.2 логика

