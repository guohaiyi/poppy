#!/usr/bin/python3
# coding=utf-8
import configparser
import os

proDir = os.path.split(os.path.realpath(__file__))[0]
configPath = os.path.join(proDir, "config.ini")


class ReadConfig:
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(configPath)

    def get_base_url(self):
        protocol = self.cf.get("HTTP", "protocol")
        ip = self.cf.get("HTTP", "ip")
        port = self.cf.get("HTTP", "port")
        base_url = protocol + '://' + ip + ':' + port
        return base_url

    def get_email(self, mail_key):
        email_value = self.cf.get("EMAIL", mail_key)
        return email_value

    def get_token(self, name):
        token_id = self.cf.get("TOKEN", name)
        return token_id

    def write_token(self, token_key, token):
        self.cf.set("TOKEN", token_key, token)
        config = open(configPath, 'w')
        with config as conf:
            self.cf.write(conf)
        config.close()

    def get_excel(self, excel_key):
        excel_vale = self.cf.get("EXCEL", excel_key)
        return excel_vale


if __name__ == "__main__":
    r = ReadConfig()
    orc_token = 'wwww'
    s = r.get_base_url()
    print(s)
