# -*- coding: UTF-8 -*-
import unittest
import json
from common.httpSet import HttpMethod
from common.readTestData import ReadTestData
from config.readConfig import ReadConfig
from common.myLog import MyLog


class TestGetDbList(unittest.TestCase):
    def setUp(self) -> None:
        self.log = MyLog()
        self.config = ReadConfig()
        self.http = HttpMethod()
        self.data = ReadTestData()
        self.sheet = "app_test_case"
        self.row = [18, 19]

    def test_db_list01(self):
        """获取Tenant DB列表"""
        # 配置请求数据
        method = self.data.get_method(self.sheet, self.row[0])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[0])
        headers = {"Content-Type": "application/json"}

        # 发送请求
        status_code, res_json = self.http.http_method(method=method, url=url, headers=headers)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象

        # 断言
        self.assertEqual(status_code, 200, msg="接口请求失败")
        self.assertTrue(dict_json["status"], msg="断言失败，实际返回结果：%s" % dict_json)

    def test_db_list02(self):
        """获取Tenant DB列表：Tenant DB列表为空"""
        # 配置请求数据
        method = self.data.get_method(self.sheet, self.row[1])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[1])
        headers = {"Content-Type": "application/json"}

        # 发送请求
        status_code, res_json = self.http.http_method(method=method, url=url, headers=headers)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象

        # 断言
        self.assertEqual(status_code, 200, msg="接口请求失败")
        self.assertFalse(dict_json["status"], msg="断言失败，实际返回结果：%s" % dict_json)
        self.assertEqual(dict_json["err"]["code"], 404, msg="断言失败，实际返回值是：%s" % dict_json["err"]["code"])
        self.assertEqual(dict_json["err"]["message"], "No records found",
                         msg="断言失败，实际返回值是：%s" % dict_json["err"]["message"])

    def tearDown(self) -> None:
        pass


if __name__ == "__main__":
    unittest.main()
