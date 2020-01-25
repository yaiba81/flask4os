import os

os.system("curl -s -o icbl.zip https://download.oracle.com/otn_software/linux/instantclient/195000/instantclient-basiclite-linux.x64-19.5.0.0.0dbru.zip && \
    unzip icbl.zip && \
    cd instantclient_19_5 && \
    export LD_LIBRARY_PATH=$(pwd) && \
    rm icbl.zip")

workers = int(os.environ.get('GUNICORN_PROCESSES', '3'))
threads = int(os.environ.get('GUNICORN_THREADS', '1'))

forwarded_allow_ips = '*'
secure_scheme_headers = { 'X-Forwarded-Proto': 'https' }
