# -*- coding: UTF-8 -*-
import json
import os

proDir = os.path.split(os.path.realpath(__file__))[0]
jsonPath = os.path.join(proDir, "../testDataFile/data.json")


class OperationJson:
    def __init__(self, file_name=None):
        if file_name:
            self.file_name = file_name
        else:
            self.file_name = jsonPath

    def key_get_data(self, key):
        """通过key值获取数据"""
        with open(self.file_name, 'r') as fp:
            data = json.load(fp)[key]
            return data
            fp.close()

    def write_data(self, w_key1, w_key2, w_data):
        """修改json数据"""
        data_dict = self.read_json()
        data_dict[w_key1][w_key2] = w_data
        with open(self.file_name, 'w') as fp:
            fp.write(json.dumps(data_dict))
            fp.close()


if __name__ == "__main__":
    file_name = "../testDataFile/header.json"
    w_key1 = "header"
    w_key2 = "Authorization"
    a = OperationJson(file_name)
    b = a.key_get_data("header1")
    print(b)
