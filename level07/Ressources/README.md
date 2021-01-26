```
ltrace ./level07

echo записывает то, что записано в LOGNAME
вызываем env, видим что в LOGNAME записано level07. Заменим на getflag
LOGNAME=\`getflag\`
./level07
```