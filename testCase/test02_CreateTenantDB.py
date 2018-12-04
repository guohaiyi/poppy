# -*- coding: UTF-8 -*-
import unittest
import json
from common.readData import ReadData
from common.httpSet import HttpMethod
from config.readConfig import ReadConfig


class CreateTenantDbTest(unittest.TestCase):
    def setUp(self):
        self.data = ReadData()
        self.http = HttpMethod()
        self.config = ReadConfig()

    def test_create_success(self):
        method = self.data.get_method(4)
        url = self.config.get_base_url() + self.data.get_url(4)
        data = self.data.get_request_data(4)
        # headers = self.data.get_headers(4)
        headers = {"Content-Type": "application/json", "Authorization": "Bearer " + self.config.get_orc_token()}
        res = self.http.http_method(method=method, url=url, data=data, headers=headers)
        dict_json = json.loads(res)  # 把json数据转换成字典对象
        self.assertTrue(dict_json["status"])

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
