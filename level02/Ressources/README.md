```
ls -l

Видим .pcap файл - это файл отчета WireShark(программа, которая 
умеет трафик анализировать

Копируем этот файл на наш компьютер

scp -P 4242 level02@127.0.0.1:/home/user/level02/level02.pcap .
chmod 777 level02.pcap
43 пакет
ПКМ>Следовать>Поток TCP
Пароль: ft_waNDReL0L (убираем точки и удаляем лишние символы)

su flag02
password: ft_waNDReL0L
getflag
```