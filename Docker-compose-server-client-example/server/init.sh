#/bin/sh
/usr/sbin/sshd -D -E /var/log/secure &
python3 ./receive.py
python3 ./server.py
