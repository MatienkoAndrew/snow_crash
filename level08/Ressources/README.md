```
./level08 token - не получается
ltrace ./level08 token
strstr("token", "token") - сравнивает название файла с "token". 
Но раз не выполняется, то создадим символическую ссылку на файл token с другим названием
ln -s ~/token /tmp/flag08
./level08 /tmp/flag08
Получаем пароль:
quif5eloekouj29ke0vouxean
su flag08
getflag
```