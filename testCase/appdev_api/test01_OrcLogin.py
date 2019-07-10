# -*- coding: UTF-8 -*-
import json
import os
import unittest
import sys

from common.httpSet import HttpMethod
from common.myLog import MyLog
from common.operationJson import OperationJson
from common.readTestData import ReadTestData
from config.readConfig import ReadConfig

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
        self.log.info(message="----------test_login01开始测试----------", name="test01_OrcLogin.py", line=30)
        # 获取测试数据
        self.log.info(message="第一步: 获取请求数据", name="test01_OrcLogin.py", line=37)
        method = self.data.get_method(self.sheet, self.row[0])
        self.log.info(message="请求方法：%s" % method, name="test01_OrcLogin.py", line=37)
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[0])
        self.log.info(message="url：%s" % url, name="test01_OrcLogin.py", line=37)
        headers = self.hea_data.get_header(self.sheet, self.row[0])
        data = self.data.get_request_data(self.sheet, self.row[0])
        self.log.info(message="请求数据：%s" % data, name="test01_OrcLogin.py", line=37)

        # 发送请求
        self.log.info(message="第二步:发送请求，获取返回数据：", name="test01_OrcLogin.py", line=37)
        status_code, res_json = self.http.http_method(method=method, url=url, data=data, headers=headers)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象
        self.log.info(message="%s" % res_json, name="test01_OrcLogin.py", line=38)
        if dict_json["status"] == True:
            orc_token = dict_json["orchestrator_admin_token"]  # 提取orc_token
            self.log.info(message="第三步：提取orc_token", name="test01_OrcLogin.py", line=42)
            self.log.info(message="%s" % orc_token, name="test01_OrcLogin.py", line=42)
            authorization = "Bearer " + orc_token
            self.json.write_data(authorization, "orc_token_header", "Authorization")  # 把orc_token写入json文件

        # 断言
        self.assertEqual(status_code, 200, msg=">>>test_login01接口请求失败")
        self.assertTrue(dict_json["status"], msg=">>>test_login01断言失败，实际返回结果：%s" % dict_json)
        self.assertEqual(dict_json["username"], "orc_admin",
                         msg=">>>test_login01断言失败，实际返回值是：%s" % dict_json["username"])
        self.log.info(message="----------test_login01测试结束----------", name="test01_OrcLogin.py", line=52)

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
        self.assertEqual(status_code, 200, msg=">>>test_login02接口请求失败")
        self.assertFalse(dict_json["status"], msg=">>>test_login02断言失败，实际返回结果：%s" % dict_json)
        self.assertEqual(dict_json["err"]["code"], 400, msg=">>>test_login02断言失败，实际返回结果：%s" % dict_json["err"]["code"])
        self.assertEqual(dict_json["err"]["message"], "Username or password error",
                         msg=">>>test_login02断言失败，实际返回结果：%s" % dict_json["err"]["message"])

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
        self.assertEqual(status_code, 200, msg=">>>接口请求失败")
        self.assertFalse(dict_json["status"], msg=">>>test_login03断言失败，实际返回结果：%s" % dict_json)
        self.assertEqual(dict_json["err"]["code"], 404, msg=">>>test_login03断言失败，实际返回结果：%s" % dict_json["err"]["code"])
        self.assertEqual(dict_json["err"]["message"], "Username does not exists",
                         msg=">>>test_login03断言失败，实际返回结果：%s" % dict_json["err"]["message"])

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
        self.assertEqual(status_code, 200, msg=">>>test_login04接口请求失败")
        self.assertFalse(dict_json["status"], msg=">>>test_login04，实际返回结果：%s" % dict_json)
        self.assertEqual(dict_json["err"]["code"], 400, msg=">>>test_login04断言失败，实际返回结果：%s" % dict_json["err"]["code"])
        self.assertEqual(dict_json["err"]["message"], "Username is needed",
                         msg=">>>test_login04断言失败，实际返回结果：%s" % dict_json["err"]["message"])

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
        self.assertEqual(status_code, 200, msg=">>>test_login05接口请求失败")
        self.assertFalse(dict_json["status"], msg=">>>test_login05断言失败，实际返回结果：%s" % dict_json)
        self.assertEqual(dict_json["err"]["code"], 400, msg=">>>test_login05断言失败，实际返回结果：%s" % dict_json["err"]["code"])
        self.assertEqual(dict_json["err"]["message"], "Password is needed",
                         msg=">>>test_login05断言失败，实际返回结果：%s" % dict_json["err"]["message"])

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
