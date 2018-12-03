# -*- coding: UTF-8 -*-
import unittest
import json
from common.readData import ReadData
from common.httpSet import HttpMethod
from config.readConfig import ReadConfig


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.data = ReadData()
        self.http = HttpMethod()
        self.config = ReadConfig()

    def test_login_success(self):
        method = self.data.get_method(2)
        url = self.config.get_base_url() + self.data.get_url(2)
        data = self.data.get_request_data(2)
        # headers = self.data.get_headers(2)
        headers = {"Content-Type": "application/json"}
        res = self.http.http_method(method=method, url=url, data=data, headers=headers)
        dict_json = json.loads(res)  # 把json数据转换成字典对象
        orc_token = dict_json["orchestrator_admin_token"]
        self.config.write_orc_token(orc_token)
        self.assertTrue(dict_json["status"])
        self.assertEqual(dict_json["username"], "orc_admin")

    def test_login_fail(self):
        method = self.data.get_method(3)
        url = self.config.get_base_url() + self.data.get_url(3)
        data = self.data.get_request_data(3)
        headers = self.data.get_headers(3)
        res = self.http.http_method(method=method, url=url, data=data, headers=headers)
        dict_json = json.loads(res)  # 把json数据转换成字典对象
        self.assertFalse(dict_json["status"])
        self.assertEqual(dict_json["err"]["code"], 400)
        self.assertEqual(dict_json["err"]["message"], "Username or password error")

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
