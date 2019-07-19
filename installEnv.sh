#!/bin/bash

# 安装jdk
yum install -y java-1.8.0-openjdk*

# 安装python3
yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel
wget https://www.python.org/ftp/python/3.7.4/Python-3.7.4.tgz
sleep 30
mkdir -p /usr/local/python3
tar -zxvf Python-3.7.4.tgz
cd Python-3.7.4
./configure --prefix=/usr/local/python3
make
make && make install
ln -s /usr/local/python3/bin/python3 /usr/bin/python3
ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3
sed -i '/PATH=$PATH/aPATH=$PATH:$HOME/bin:/usr/local/python3/bin' ~/.bash_profile


# 安装ffmpeg
yum install epel-release -y
rpm --import http://li.nux.ro/download/nux/RPM-GPG-KEY-nux.ro
rpm -Uvh http://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-release-0-5.el7.nux.noarch.rpm
yum install ffmpeg ffmpeg-devel -y