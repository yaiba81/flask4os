import os

os.system("curl -s -o icbl.zip https://download.oracle.com/otn_software/linux/instantclient/195000/instantclient-basiclite-linux.x64-19.5.0.0.0dbru.zip && \
    unzip icbl.zip && \
    cp -r instantclient_19_5 /opt/app-root/bin/instantclient_19_5")

os.system("cd /opt/app-root/bin && \
    wget http://mirror.centos.org/centos/7/os/x86_64/Packages/libaio-0.3.109-13.el7.x86_64.rpm && \
    rpm2cpio libaio-0.3.109-13.el7.x86_64.rpm | cpio -idmv")

workers = int(os.environ.get('GUNICORN_PROCESSES', '3'))
threads = int(os.environ.get('GUNICORN_THREADS', '1'))

forwarded_allow_ips = '*'
secure_scheme_headers = { 'X-Forwarded-Proto': 'https' }
