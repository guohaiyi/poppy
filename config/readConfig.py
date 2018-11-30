# -*- coding: UTF-8 -*-
import configparser
import os

proDir = os.path.split(os.path.realpath(__file__))[0]
configPath = os.path.join(proDir, "config.ini")


class ReadConfig:
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(configPath)

    def get_base_url(self):
        base_url = self.cf.get("HTTP", "base_url")
        return base_url


if __name__ == "__main__":
    r = ReadConfig()
    s = r.get_base_url()
    print(s)
