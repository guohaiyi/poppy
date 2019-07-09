# -*- coding: UTF-8 -*-
import unittest
import os
import json
from common.httpSet import HttpMethod
from common.readTestData import ReadTestData
from config.readConfig import ReadConfig
from common.myLog import MyLog
from common.operationJson import OperationJson

proDir = os.path.split(os.path.realpath(__file__))[0]
file_name = os.path.join(proDir, "../../testDataFile/orchestrator_account.json")


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.data = ReadTestData(file_name)
        self.hea_data = ReadTestData()
        self.http = HttpMethod()
        self.config = ReadConfig()
        self.log = MyLog()
        self.json = OperationJson()
        self.sheet = 'app_test_case'
        self.row = [2, 3, 4, 5, 6]

    def test_login01(self):
        """orc admin正常登录"""
        # 获取测试数据
        method = self.data.get_method(self.sheet, self.row[0])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[0])
        headers = self.hea_data.get_header(self.sheet, self.row[0])
        data = self.data.get_request_data(self.sheet, self.row[0])

        # 发送请求
        status_code, res_json = self.http.http_method(method=method, url=url, data=data, headers=headers)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象
        if dict_json["status"] == True:
            orc_token = dict_json["orchestrator_admin_token"]  # 提取orc_token
            authorization = "Bearer " + orc_token
            self.json.write_data(authorization, "orc_token_header", "Authorization")  # 把orc_token写入json文件

        # 断言
        self.assertEqual(status_code, 200, msg="接口请求失败")
        self.assertTrue(dict_json["status"], msg="断言失败，实际返回结果：%s" % dict_json)
        self.assertEqual(dict_json["username"], "orc_admin", msg="断言失败，实际返回值是：%s" % dict_json["username"])

    def test_login02(self):
        """登录失败，密码错误"""
        # 获取测试数据
        method = self.data.get_method(self.sheet, self.row[1])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[1])
        headers = self.hea_data.get_header(self.sheet, self.row[1])
        data = self.data.get_request_data(self.sheet, self.row[1])

        # 发送请求
        status_code, res_json = self.http.http_method(method=method, url=url, data=data, headers=headers)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象

        # 断言
        self.assertEqual(status_code, 200, msg="接口请求失败")
        self.assertFalse(dict_json["status"], msg="断言失败，实际返回结果：%s" % dict_json)
        self.assertEqual(dict_json["err"]["code"], 400, msg="断言失败，实际返回结果：%s" % dict_json["err"]["code"])
        self.assertEqual(dict_json["err"]["message"], "Username or password error",
                         msg="断言失败，实际返回结果：%s" % dict_json["err"]["message"])

    def test_login03(self):
        """登录失败，账户不存在"""
        # 获取测试数据
        method = self.data.get_method(self.sheet, self.row[2])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[2])
        headers = self.hea_data.get_header(self.sheet, self.row[2])
        data = self.data.get_request_data(self.sheet, self.row[2])

        # 发送请求
        status_code, res_json = self.http.http_method(method=method, url=url, data=data, headers=headers)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象

        # 断言
        self.assertEqual(status_code, 200, msg="接口请求失败")
        self.assertFalse(dict_json["status"], msg="断言失败，实际返回结果：%s" % dict_json)
        self.assertEqual(dict_json["err"]["code"], 404, msg="断言失败，实际返回结果：%s" % dict_json["err"]["code"])
        self.assertEqual(dict_json["err"]["message"], "Username does not exists",
                         msg="断言失败，实际返回结果：%s" % dict_json["err"]["message"])

    # @unittest.skip("跳过测试")
    def test_login04(self):
        """登录失败，缺少username字段"""
        # 获取测试数据
        method = self.data.get_method(self.sheet, self.row[3])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[3])
        headers = self.hea_data.get_header(self.sheet, self.row[3])
        data = self.data.get_request_data(self.sheet, self.row[3])

        # 发送请求
        status_code, res_json = self.http.http_method(method=method, url=url, data=data, headers=headers)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象

        # 断言
        self.assertEqual(status_code, 200, msg="接口请求失败")
        self.assertFalse(dict_json["status"], msg="断言失败，实际返回结果：%s" % dict_json)
        self.assertEqual(dict_json["err"]["code"], 400, msg="断言失败，实际返回结果：%s" % dict_json["err"]["code"])
        self.assertEqual(dict_json["err"]["message"], "Username is needed",
                         msg="断言失败，实际返回结果：%s" % dict_json["err"]["message"])

    def test_login05(self):
        """登录失败，缺少password字段"""
        # 获取测试数据
        method = self.data.get_method(self.sheet, self.row[4])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[4])
        headers = self.hea_data.get_header(self.sheet, self.row[4])
        data = self.data.get_request_data(self.sheet, self.row[4])

        # 发送请求
        status_code, res_json = self.http.http_method(method=method, url=url, data=data, headers=headers)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象

        # 断言
        self.assertEqual(status_code, 200, msg="接口请求失败")
        self.assertFalse(dict_json["status"], msg="断言失败，实际返回结果：%s" % dict_json)
        self.assertEqual(dict_json["err"]["code"], 400, msg="断言失败，实际返回结果：%s" % dict_json["err"]["code"])
        self.assertEqual(dict_json["err"]["message"], "Password is needed",
                         msg="断言失败，实际返回结果：%s" % dict_json["err"]["message"])

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
