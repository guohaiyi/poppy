# -*- coding: UTF-8 -*-
import unittest
import json
import os
from common.readTestData import ReadTestData
from common.httpSet import HttpMethod
from config.readConfig import ReadConfig
from common.myLog import MyLog

proDir = os.path.split(os.path.realpath(__file__))[0]
file_name = os.path.join(proDir, "../../testDataFile/tenant_db.json")


class CreateTenantDbTest(unittest.TestCase):
    def setUp(self):
        self.data = ReadTestData(file_name)
        self.http = HttpMethod()
        self.config = ReadConfig()
        self.log = MyLog()
        self.sheet = 'app_test_case'
        self.row = [12, 13, 14, 15, 16, 17]

    def test_create_db01(self):
        """创建Tenant DB，不创建autolive"""
        # 设置请求数据
        method = self.data.get_method(self.sheet, self.row[0])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[0])
        data = self.data.get_request_data(self.sheet, self.row[0])
        headers = {"Content-Type": "application/json", "Authorization": "Bearer " + self.config.get_token('orc_token')}

        # 发送请求
        status_code, res_json = self.http.http_method(method=method, url=url, data=data, headers=headers)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象

        # 断言
        self.assertEqual(status_code, 200, msg="两个值不相等")
        self.assertTrue(dict_json["status"], msg='>>>创建DB失败，实际返回结果：%s' % dict_json)

    def test_create_db02(self):
        """创建成功，并创建autolive"""
        # 设置请求数据
        method = self.data.get_method(self.sheet, self.row[1])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[1])
        data = self.data.get_request_data(self.sheet, self.row[1])
        headers = {"Content-Type": "application/json", "Authorization": "Bearer " + self.config.get_token('orc_token')}

        # 发送请求
        status_code, res_json = self.http.http_method(method=method, url=url, data=data, headers=headers)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象

        # 断言
        self.assertEqual(status_code, 200, msg="两个值不相等")
        self.assertTrue(dict_json["status"], msg='>>>创建DB失败，实际返回结果：%s' % dict_json)

    def test_create_db03(self):
        """创建失败：缺少tenant name"""
        # 设置请求数据
        method = self.data.get_method(self.sheet, self.row[2])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[2])
        data = self.data.get_request_data(self.sheet, self.row[2])
        headers = {"Content-Type": "application/json", "Authorization": "Bearer " + self.config.get_token('orc_token')}

        # 发送请求
        status_code, res_json = self.http.http_method(method=method, url=url, data=data, headers=headers)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象

        # 断言
        self.assertEqual(status_code, 200, msg="两个值不相等")
        self.assertTrue(dict_json["status"], msg='>>>创建DB失败，实际返回结果：%s' % dict_json)

    def test_create_db04(self):
        """创建失败：缺少db name"""
        # 设置请求数据
        method = self.data.get_method(self.sheet, self.row[3])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[4])
        data = self.data.get_request_data(self.sheet, self.row[3])
        headers = {"Content-Type": "application/json", "Authorization": "Bearer " + self.config.get_token('orc_token')}

        # 发送请求
        status_code, res_json = self.http.http_method(method=method, url=url, data=data, headers=headers)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象

        # 断言
        self.assertEqual(status_code, 200, msg="两个值不相等")
        self.assertTrue(dict_json["status"], msg='>>>创建DB失败，实际返回结果：%s' % dict_json)

    def test_create_db05(self):
        """创建失败：tenant name已被占用"""
        # 设置请求数据
        method = self.data.get_method(self.sheet, self.row[4])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[4])
        data = self.data.get_request_data(self.sheet, self.row[4])
        headers = {"Content-Type": "application/json", "Authorization": "Bearer " + self.config.get_token('orc_token')}

        # 发送请求
        status_code, res_json = self.http.http_method(method=method, url=url, data=data, headers=headers)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象

        # 断言
        self.assertEqual(status_code, 200, msg="两个值不相等")
        self.assertTrue(dict_json["status"], msg='>>>创建DB失败，实际返回结果：%s' % dict_json)

    def test_create_db06(self):
        """创建失败：db name已被占用"""
        # 设置请求数据
        method = self.data.get_method(self.sheet, self.row[5])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[5])
        data = self.data.get_request_data(self.sheet, self.row[5])
        headers = {"Content-Type": "application/json", "Authorization": "Bearer " + self.config.get_token('orc_token')}

        # 发送请求
        status_code, res_json = self.http.http_method(method=method, url=url, data=data, headers=headers)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象

        # 断言
        self.assertEqual(status_code, 200, msg="两个值不相等")
        self.assertTrue(dict_json["status"], msg='>>>创建DB失败，实际返回结果：%s' % dict_json)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
