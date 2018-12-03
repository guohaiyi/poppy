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

    def get_orc_token(self):
        orc_token = self.cf.get("Orchestrator_admin_token", "Orc_token")
        return orc_token

    def get_tenant_token(self):
        tenant_token = self.cf.get("Tenant_admin_token", "tenant_token")
        return tenant_token

    def write_orc_token(self, orc_token):
        self.cf.set("Orchestrator_admin_token", "Orc_token", orc_token)
        with open(configPath, 'w') as conf:
            self.cf.write(conf)

    def write_tenant_token(self, tenant_token):
        self.cf.set("Tenant_admin_token", "tenant_token", tenant_token)
        with open(configPath, 'w') as conf:
            self.cf.write(conf)




if __name__ == "__main__":
    r = ReadConfig()
    s = r.write_orc_token("aaaadasdcdcdcdcdcdcdcdcdcaaaaa")
    print(s)
