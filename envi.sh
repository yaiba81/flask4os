#!/bin/sh

curl -s -o icbl.zip https://download.oracle.com/otn_software/linux/instantclient/195000/instantclient-basiclite-linux.x64-19.5.0.0.0dbru.zip && \
    unzip icbl.zip
    
wget http://mirror.centos.org/centos/7/os/x86_64/Packages/libaio-0.3.109-13.el7.x86_64.rpm && \
    rpm2cpio libaio-0.3.109-13.el7.x86_64.rpm | cpio -idmv

cd lib64 && \
    cp -r libaio.so.1.0.1 /opt/app-root/src/instantclient_19_5

cd  /opt/app-root/src/instantclient_19_5 && \
    ln -s libaio.so.1.0.1 libaio.so.1

source /opt/app-root/etc/generate_container_user

export LD_LIBRARY_PATH=/opt/app-root/src/instantclient_19_5:$LD_LIBRARY_PATH
