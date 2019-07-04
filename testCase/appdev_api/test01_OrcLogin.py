# -*- coding: UTF-8 -*-
import unittest
import json
import os
from common.readTestData import ReadTestData
from common.httpSet import HttpMethod
from config.readConfig import ReadConfig
from common.myLog import MyLog

proDir = os.path.split(os.path.realpath(__file__))[0]
file_name = os.path.join(proDir, "../../testDataFile/orchestrator_account.json")


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.data = ReadTestData(file_name)
        self.http = HttpMethod()
        self.config = ReadConfig()
        self.log = MyLog()
        self.sheet = 'app_test_case'

    def test_login_success(self):
        """orc admin正常登录"""
        # 获取测试数据
        method = self.data.get_method(self.sheet, 2)
        url = self.config.get_base_url() + self.data.get_url(self.sheet, 2)
        data = self.data.get_request_data(self.sheet, 2)
        headers = {"Content-Type": "application/json"}
        # 发送请求
        status_code, res_json = self.http.http_method(method=method, url=url, data=data, headers=headers)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象
        if dict_json["status"] == True:
            orc_token = dict_json["orchestrator_admin_token"]  # 提取orc_token
            self.config.write_token("orc_token", orc_token)  # 把orc_token写入配置文件
        # 断言
        self.assertEqual(status_code, 200, msg="接口请求失败")
        self.assertTrue(dict_json["status"], msg="断言失败，实际返回结果：%s" % dict_json)
        self.assertEqual(dict_json["username"], "orc_admin", msg="断言失败，实际返回值是：%s" % dict_json["username"])

    def test_login_fail(self):
        """登录失败，密码错误"""
        # 获取测试数据
        method = self.data.get_method(self.sheet, 3)
        url = self.config.get_base_url() + self.data.get_url(self.sheet, 3)
        data = self.data.get_request_data(self.sheet, 3)
        headers = {"Content-Type": "application/json"}
        # 发送请求
        status_code, res_json = self.http.http_method(method=method, url=url, data=data, headers=headers)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象
        # 断言
        self.assertEqual(status_code, 200, msg="接口请求失败")
        self.assertFalse(dict_json["status"], msg="断言失败，实际返回结果：%s" % dict_json)
        self.assertEqual(dict_json["err"]["code"], 400, msg="断言失败，实际返回结果：%s" % dict_json["err"]["code"])
        self.assertEqual(dict_json["err"]["message"], "Username or password error",
                         msg="断言失败，实际返回结果：%s" % dict_json["err"]["message"])

    def test_login_fail_not(self):
        """登录失败，账户不存在"""
        # 获取测试数据
        method = self.data.get_method(self.sheet, 4)
        url = self.config.get_base_url() + self.data.get_url(self.sheet, 4)
        data = self.data.get_request_data(self.sheet, 4)
        headers = {"Content-Type": "application/json"}
        # 发送请求
        status_code, res_json = self.http.http_method(method=method, url=url, data=data, headers=headers)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象
        # 断言
        self.assertEqual(status_code, 200, msg="接口请求失败")
        self.assertFalse(dict_json["status"], msg="断言失败，实际返回结果：%s" % dict_json)
        self.assertEqual(dict_json["err"]["code"], 404, msg="断言失败，实际返回结果：%s" % dict_json["err"]["code"])
        self.assertEqual(dict_json["err"]["message"], "Username does not exists",
                         msg="断言失败，实际返回结果：%s" % dict_json["err"]["message"])

    @unittest.skip("跳过测试")
    def test_login_fail_lack_name(self):
        """登录失败，缺少username字段"""
        # 获取测试数据
        method = self.data.get_method(self.sheet, 5)
        url = self.config.get_base_url() + self.data.get_url(self.sheet, 5)
        data = self.data.get_request_data(self.sheet, 5)
        headers = {"Content-Type": "application/json"}
        # 发送请求
        status_code, res_json = self.http.http_method(method=method, url=url, data=data, headers=headers)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象
        # 断言
        self.assertEqual(status_code, 200, msg="接口请求失败")
        self.assertFalse(dict_json["status"], msg="断言失败，实际返回结果：%s" % dict_json)
        self.assertEqual(dict_json["err"]["code"], 400, msg="断言失败，实际返回结果：%s" % dict_json["err"]["code"])
        self.assertEqual(dict_json["err"]["message"], "Username is needed",
                         msg="断言失败，实际返回结果：%s" % dict_json["err"]["message"])

    def test_login_lack_pw(self):
        """登录失败，缺少password字段"""
        # 获取测试数据
        method = self.data.get_method(self.sheet, 6)
        url = self.config.get_base_url() + self.data.get_url(self.sheet, 6)
        data = self.data.get_request_data(self.sheet, 6)
        headers = {"Content-Type": "application/json"}
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
