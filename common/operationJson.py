# -*- coding: UTF-8 -*-
import json
import os

proDir = os.path.split(os.path.realpath(__file__))[0]
jsonPath = os.path.join(proDir, "../testDataFile/data.json")


# jsonPath = "../testDataFile/data.json"

class OperationJson:
    def __init__(self, file_name=None):
        if file_name:
            self.file_name = file_name
        else:
            self.file_name = jsonPath

    def read_json(self):
        with open(self.file_name, 'r') as fp:
            data = json.load(fp)
            return data

    def key_get_data(self, key):
        data = self.read_json()[key]
        return data

    def key_get_headers(self, key):
        headers = self.read_json()[key]
        return headers


if __name__ == "__main__":
    file_name = "../testDataFile/tenant_db.json"
    a = OperationJson(file_name)
    b = a.key_get_headers("tenant_db")
    print(b)
