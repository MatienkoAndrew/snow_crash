1) cat /etc/passwd - база данных пользователей с разными полями

John the Ripper - восстанавливает пароль по хешу, 
перебирая все возможные варианты

https://www.openwall.com/john/

```
cd run
echo 42hDRfypTqqnw > lol
john.exe lol --show
```
> Password : abcdefg

```
su flag01
password: abcdefg
getflag
```