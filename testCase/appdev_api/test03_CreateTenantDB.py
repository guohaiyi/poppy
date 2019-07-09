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
        self.hea_data = ReadTestData()
        self.http = HttpMethod()
        self.config = ReadConfig()
        self.log = MyLog()
        self.sheet = 'app_test_case'
        self.row = [12, 13, 14, 15, 16, 17, 18, 19]

    def test01_get_db_list(self):
        """获取Tenant DB列表：Tenant DB列表为空"""
        # 设置请求数据
        method = self.data.get_method(self.sheet, self.row[6])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[6])
        headers = self.hea_data.get_header(self.sheet, self.row[6])

        # 发送请求
        status_code, res_json = self.http.http_method(method=method, url=url, headers=headers)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象

        # 断言
        self.assertEqual(status_code, 200, msg="两个值不相等")
        self.assertFalse(dict_json["status"], msg='>>>创建DB失败，实际返回结果：%s' % dict_json)
        self.assertEqual(dict_json["err"]["code"], 404, msg="断言失败，实际返回结果：%s" % dict_json["err"]["code"])
        self.assertEqual(dict_json["err"]["message"], "No records found",
                         msg="断言失败，实际返回结果：%s" % dict_json["err"]["message"])

    def test02_create_db(self):
        """创建Tenant DB，不创建autolive"""
        # 设置请求数据
        method = self.data.get_method(self.sheet, self.row[0])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[0])
        data = self.data.get_request_data(self.sheet, self.row[0])
        headers = self.hea_data.get_header(self.sheet, self.row[0])

        # 发送请求
        status_code, res_json = self.http.http_method(method=method, url=url, data=data, headers=headers)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象

        # 断言
        self.assertEqual(status_code, 200, msg="两个值不相等")
        self.assertTrue(dict_json["status"], msg='>>>创建DB失败，实际返回结果：%s' % dict_json)

    def test03_create_db(self):
        """创建成功，并创建autolive"""
        # 设置请求数据
        method = self.data.get_method(self.sheet, self.row[1])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[1])
        data = self.data.get_request_data(self.sheet, self.row[1])
        headers = self.hea_data.get_header(self.sheet, self.row[1])

        # 发送请求
        status_code, res_json = self.http.http_method(method=method, url=url, data=data, headers=headers)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象

        # 断言
        self.assertEqual(status_code, 200, msg="两个值不相等")
        self.assertTrue(dict_json["status"], msg='>>>创建DB失败，实际返回结果：%s' % dict_json)

    def test04_create_db(self):
        """创建失败：缺少tenant name"""
        # 设置请求数据
        method = self.data.get_method(self.sheet, self.row[2])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[2])
        data = self.data.get_request_data(self.sheet, self.row[2])
        headers = self.hea_data.get_header(self.sheet, self.row[2])

        # 发送请求
        status_code, res_json = self.http.http_method(method=method, url=url, data=data, headers=headers)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象

        # 断言
        self.assertEqual(status_code, 200, msg="两个值不相等")
        self.assertFalse(dict_json["status"], msg="断言失败，实际返回结果：%s" % dict_json)
        self.assertEqual(dict_json["err"]["code"], 400, msg="断言失败，实际返回结果：%s" % dict_json["err"]["code"])
        self.assertEqual(dict_json["err"]["message"], "Provide tenant name",
                         msg="断言失败，实际返回结果：%s" % dict_json["err"]["message"])

    def test05_create_db(self):
        """创建失败：缺少db name"""
        # 设置请求数据
        method = self.data.get_method(self.sheet, self.row[3])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[4])
        data = self.data.get_request_data(self.sheet, self.row[3])
        headers = self.hea_data.get_header(self.sheet, self.row[3])

        # 发送请求
        status_code, res_json = self.http.http_method(method=method, url=url, data=data, headers=headers)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象

        # 断言
        self.assertEqual(status_code, 200, msg="两个值不相等")
        self.assertFalse(dict_json["status"], msg="断言失败，实际返回结果：%s" % dict_json)
        self.assertEqual(dict_json["err"]["code"], 400, msg="断言失败，实际返回结果：%s" % dict_json["err"]["code"])
        self.assertEqual(dict_json["err"]["message"], "Provide db",
                         msg="断言失败，实际返回结果：%s" % dict_json["err"]["message"])

    def test06_create_db(self):
        """创建失败：tenant name已被占用"""
        # 设置请求数据
        method = self.data.get_method(self.sheet, self.row[4])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[4])
        data = self.data.get_request_data(self.sheet, self.row[4])
        headers = self.hea_data.get_header(self.sheet, self.row[4])

        # 发送请求
        status_code, res_json = self.http.http_method(method=method, url=url, data=data, headers=headers)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象

        # 断言
        self.assertEqual(status_code, 200, msg="两个值不相等")
        self.assertFalse(dict_json["status"], msg="断言失败，实际返回结果：%s" % dict_json)
        self.assertEqual(dict_json["err"]["code"], 400, msg="断言失败，实际返回结果：%s" % dict_json["err"]["code"])
        self.assertEqual(dict_json["err"]["message"], "Tenant name/DB already exists",
                         msg="断言失败，实际返回结果：%s" % dict_json["err"]["message"])

    def test07_create_db(self):
        """创建失败：db name已被占用"""
        # 设置请求数据
        method = self.data.get_method(self.sheet, self.row[5])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[5])
        data = self.data.get_request_data(self.sheet, self.row[5])
        headers = self.hea_data.get_header(self.sheet, self.row[5])

        # 发送请求
        status_code, res_json = self.http.http_method(method=method, url=url, data=data, headers=headers)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象

        # 断言
        self.assertEqual(status_code, 200, msg="两个值不相等")
        self.assertFalse(dict_json["status"], msg="断言失败，实际返回结果：%s" % dict_json)
        self.assertEqual(dict_json["err"]["code"], 400, msg="断言失败，实际返回结果：%s" % dict_json["err"]["code"])
        self.assertEqual(dict_json["err"]["message"], "Tenant name/DB already exists",
                         msg="断言失败，实际返回结果：%s" % dict_json["err"]["message"])

    def test08_get_db_list(self):
        """获取Tenant DB列表"""
        # 设置请求数据
        method = self.data.get_method(self.sheet, self.row[7])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[7])
        headers = self.hea_data.get_header(self.sheet, self.row[7])

        # 发送请求
        status_code, res_json = self.http.http_method(method=method, url=url, headers=headers)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象

        # 断言
        self.assertEqual(status_code, 200, msg="两个值不相等")
        self.assertTrue(dict_json["status"], msg='>>>创建DB失败，实际返回结果：%s' % dict_json)
        self.assertIs("_id", dict_json["results"][0])
        self.assertEqual(dict_json["results"][0]["tenant_name"], "autotest",
                         msg="断言失败，实际返回结果：%s" % dict_json["results"][0]["tenant_name"])
        self.assertEqual(dict_json["results"][1]["tenant_name"], "test_autolive",
                         msg="断言失败，实际返回结果：%s" % dict_json["results"][1]["tenant_name"])

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
