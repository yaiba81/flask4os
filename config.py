import os

os.system("curl -s -o icbl.zip https://download.oracle.com/otn_software/linux/instantclient/195000/instantclient-basiclite-linux.x64-19.5.0.0.0dbru.zip && \
    unzip icbl.zip")
os.system("wget http://mirror.centos.org/centos/7/os/x86_64/Packages/libaio-0.3.109-13.el7.x86_64.rpm && \
    rpm2cpio libaio-0.3.109-13.el7.x86_64.rpm | cpio -idmv")
os.system("cd lib64 && \
    cp -r libaio.so.1.0.1 /opt/app-root/src/instantclient_19_5")
os.system("cd  /opt/app-root/src/instantclient_19_5 && \
    ln -s libaio.so.1.0.1 libaio.so.1")
os.system("source /opt/app-root/etc/generate_container_user")
os.system("cd /opt/app-root/src/instantclient_19_5 && \
    export LD_LIBRARY_PATH=/opt/app-root/src/instantclient_19_5:$LD_LIBRARY_PATH")

workers = int(os.environ.get('GUNICORN_PROCESSES', '3'))
threads = int(os.environ.get('GUNICORN_THREADS', '1'))

forwarded_allow_ips = '*'
secure_scheme_headers = { 'X-Forwarded-Proto': 'https' }
