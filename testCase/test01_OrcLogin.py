# -*- coding: UTF-8 -*-
import unittest
import json
import os
from common.readData import ReadData
from common.httpSet import HttpMethod
from config.readConfig import ReadConfig
from common.myLog import MyLog
from common.operationExcel import OperationExcel

proDir = os.path.split(os.path.realpath(__file__))[0]
file_name = os.path.join(proDir, "../testDataFile/orchestrator_account.json")


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.data = ReadData(file_name)
        self.http = HttpMethod()
        self.config = ReadConfig()
        self.log = MyLog()
        self.oper_excel = OperationExcel()

    def test_login_success(self):
        """orc admin正常登录"""
        case_id = self.data.get_case_id(2)
        case_title = self.data.get_case_title(2)
        # 获取测试数据
        method = self.data.get_method(2)
        url = self.config.get_base_url() + self.data.get_url(2)
        data = self.data.get_request_data(2)
        headers = {"Content-Type": "application/json"}
        # 发送请求
        status_code, res_json = self.http.http_method(method=method, url=url, data=data, headers=headers)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象
        orc_token = dict_json["orchestrator_admin_token"]  # 提取orc_token
        self.config.write_orc_token(orc_token)  # 把orc_token写入配置文件
        # self.oper_excel.write_data('K', 2, res_json)  # 把实际返回结果写入Excel
        # 断言
        self.assertEqual(status_code, 200, msg="接口请求失败")
        self.assertTrue(dict_json["status"], msg="断言失败，实际返回结果：%s" % dict_json)
        self.assertEqual(dict_json["username"], "orc_admin", msg="断言失败，实际返回值是：%s" % dict_json["username"])
        # 打印Log
        self.log.info("用例编号：%s，用例标题：%s-测试通过" % (case_id, case_title))

    def test_login_fail(self):
        """登录失败，密码错误"""
        case_id = self.data.get_case_id(3)
        case_title = self.data.get_case_title(3)
        method = self.data.get_method(3)
        url = self.config.get_base_url() + self.data.get_url(3)
        data = self.data.get_request_data(3)
        headers = {"Content-Type": "application/json"}
        # 发送请求
        status_code, res_json = self.http.http_method(method=method, url=url, data=data, headers=headers)
        # self.oper_excel.write_data('K', 3, res_json)  # 把实际返回结果写入Excel
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象
        # 断言
        self.assertEqual(status_code, 200, msg="接口请求失败")
        self.assertFalse(dict_json["status"], msg="断言失败，实际返回结果：%s" % dict_json)
        self.assertEqual(dict_json["err"]["code"], 400, msg="断言失败，实际返回结果：%s" % dict_json["err"]["code"])
        self.assertEqual(dict_json["err"]["message"], "Username or password error",
                         msg="断言失败，实际返回结果：%s" % dict_json["err"]["message"])

    def test_login_fail_not(self):
        """登录失败，账户不存在"""
        case_id = self.data.get_case_id(4)
        case_title = self.data.get_case_title(4)
        method = self.data.get_method(4)
        url = self.config.get_base_url() + self.data.get_url(4)
        data = self.data.get_request_data(4)
        headers = {"Content-Type": "application/json"}
        # 发送请求
        status_code, res_json = self.http.http_method(method=method, url=url, data=data, headers=headers)
        # self.oper_excel.write_data('K', 4, res_json)  # 把实际返回结果写入Excel
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象
        # 断言
        self.assertEqual(status_code, 200, msg="接口请求失败")
        self.assertFalse(dict_json["status"], msg="断言失败，实际返回结果：%s" % dict_json)
        self.assertEqual(dict_json["err"]["code"], 404, msg="断言失败，实际返回结果：%s" % dict_json["err"]["code"])
        self.assertEqual(dict_json["err"]["message"], "Username does not exists",
                         msg="断言失败，实际返回结果：%s" % dict_json["err"]["message"])

    def test_login_fail_lack_name(self):
        """登录失败，缺少username字段"""
        case_id = self.data.get_case_id(5)
        case_title = self.data.get_case_title(5)
        method = self.data.get_method(5)
        url = self.config.get_base_url() + self.data.get_url(5)
        data = self.data.get_request_data(5)
        headers = {"Content-Type": "application/json"}
        # 发送请求
        status_code, res_json = self.http.http_method(method=method, url=url, data=data, headers=headers)
        # self.oper_excel.write_data('K', 5, res_json)  # 把实际返回结果写入Excel
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象
        # 断言
        self.assertEqual(status_code, 200, msg="接口请求失败")
        self.assertFalse(dict_json["status"], msg="断言失败，实际返回结果：%s" % dict_json)
        self.assertEqual(dict_json["err"]["code"], 400, msg="断言失败，实际返回结果：%s" % dict_json["err"]["code"])
        self.assertEqual(dict_json["err"]["message"], "Username is needed",
                         msg="断言失败，实际返回结果：%s" % dict_json["err"]["message"])

    def test_login_lack_pw(self):
        """登录失败，缺少password字段"""
        case_id = self.data.get_case_id(6)
        case_title = self.data.get_case_title(6)
        method = self.data.get_method(6)
        url = self.config.get_base_url() + self.data.get_url(6)
        data = self.data.get_request_data(6)
        headers = {"Content-Type": "application/json"}
        # 发送请求
        status_code, res_json = self.http.http_method(method=method, url=url, data=data, headers=headers)
        # self.oper_excel.write_data('K', 6, res_json)  # 把实际返回结果写入Excel
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
