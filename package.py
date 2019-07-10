#!/usr/bin/python3
# coding=utf-8
import os

count = 2
while count:
    try:
        import requests

        print("已检测到requests模块,无需安装--- OK")
        break
    except:
        print("未检测到requests模块，现在开始安装......")
        os.system('pip3 install requests')
        count -= 1
