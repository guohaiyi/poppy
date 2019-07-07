# -*- coding: UTF-8 -*-
import unittest
import os
import json
from common.httpSet import HttpMethod
from common.readTestData import ReadTestData
from config.readConfig import ReadConfig
from common.myLog import MyLog

proDir = os.path.split(os.path.realpath(__file__))[0]
file_name = os.path.join(proDir, "../../testDataFile/orchestrator_account.json")


class TestUpdateOrcPw(unittest.TestCase):
    def setUp(self) -> None:
        self.log = MyLog()
        self.config = ReadConfig()
        self.http = HttpMethod()
        self.data = ReadTestData(file_name)
        self.sheet = "app_test_case"
        self.row = [7, 8, 9, 10, 11]

    def test_update01(self):
        """更新密码失败：旧密码错误"""
        # 配置请求数据
        method = self.data.get_method(self.sheet, self.row[0])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[0])
        headers = {"Content-Type": "application/json"}
        data = self.data.get_request_data(self.sheet, self.row[0])

        # 发送请求
        status_code, res_json = self.http.http_method(method=method, url=url, headers=headers, data=data)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象

        # 断言
        self.assertEqual(status_code, 200, msg="接口请求失败")
        self.assertFalse(dict_json["status"], msg="断言失败，实际返回结果：%s" % dict_json)
        self.assertEqual(dict_json["err"]["code"], 400, msg="断言失败，实际返回值是：%s" % dict_json["err"]["code"])
        self.assertEqual(dict_json["err"]["message"], "Username or password error",
                         msg="断言失败，实际返回值是：%s" % dict_json["err"]["message"])

    def test_update02(self):
        # 配置请求数据
        method = self.data.get_method(self.sheet, self.row[1])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[1])
        headers = {"Content-Type": "application/json"}
        data = self.data.get_request_data(self.sheet, self.row[1])

        # 发送请求
        status_code, res_json = self.http.http_method(method=method, url=url, headers=headers, data=data)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象

        # 断言
        self.assertEqual(status_code, 200, msg="接口请求失败")
        self.assertFalse(dict_json["status"], msg="断言失败，实际返回结果：%s" % dict_json)
        self.assertEqual(dict_json["err"]["code"], 404, msg="断言失败，实际返回值是：%s" % dict_json["err"]["code"])
        self.assertEqual(dict_json["err"]["message"], "Username does not exists",
                         msg="断言失败，实际返回值是：%s" % dict_json["err"]["message"])

    def test_update03(self):
        # 配置请求数据
        method = self.data.get_method(self.sheet, self.row[2])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[2])
        headers = {"Content-Type": "application/json"}
        data = self.data.get_request_data(self.sheet, self.row[2])

        # 发送请求
        status_code, res_json = self.http.http_method(method=method, url=url, headers=headers, data=data)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象

        # 断言
        self.assertEqual(status_code, 200, msg="接口请求失败")
        self.assertFalse(dict_json["status"], msg="断言失败，实际返回结果：%s" % dict_json)
        self.assertEqual(dict_json["err"]["code"], 400, msg="断言失败，实际返回值是：%s" % dict_json["err"]["code"])
        self.assertEqual(dict_json["err"]["message"], "New password is needed",
                         msg="断言失败，实际返回值是：%s" % dict_json["err"]["message"])

    def test_update04(self):
        # 配置请求数据
        method = self.data.get_method(self.sheet, self.row[3])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[3])
        headers = {"Content-Type": "application/json"}
        data = self.data.get_request_data(self.sheet, self.row[3])

        # 发送请求
        status_code, res_json = self.http.http_method(method=method, url=url, headers=headers, data=data)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象

        # 断言
        self.assertEqual(status_code, 200, msg="接口请求失败")
        self.assertFalse(dict_json["status"], msg="断言失败，实际返回结果：%s" % dict_json)
        self.assertEqual(dict_json["err"]["code"], 400, msg="断言失败，实际返回值是：%s" % dict_json["err"]["code"])
        self.assertEqual(dict_json["err"]["message"], "Current password is needed",
                         msg="断言失败，实际返回值是：%s" % dict_json["err"]["message"])

    def test_update05(self):
        # 配置请求数据
        method = self.data.get_method(self.sheet, self.row[4])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[4])
        headers = {"Content-Type": "application/json"}
        data = self.data.get_request_data(self.sheet, self.row[4])

        # 发送请求
        status_code, res_json = self.http.http_method(method=method, url=url, headers=headers, data=data)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象

        # 断言
        self.assertEqual(status_code, 200, msg="接口请求失败")
        self.assertTrue(dict_json["status"], msg="断言失败，实际返回结果：%s" % dict_json)

        # 验证修改密码成功
        if dict_json["status"] == True:
            self.check_new_login()
        else:
            self.log.error("重新获取orc_admin_token失败")

    def tearDown(self) -> None:
        pass

    def check_new_login(self):
        """重新获取orc_admin_token"""
        # 获取测试数据
        method = self.data.get_method(self.sheet, 2)
        url = self.config.get_base_url() + self.data.get_url(self.sheet, 2)
        data = self.data.get_rely_data(self.sheet, self.row[4])
        headers = {"Content-Type": "application/json"}
        # 发送请求
        status_code, res_json = self.http.http_method(method=method, url=url, data=data, headers=headers)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象
        if dict_json["status"] == True:
            orc_token = dict_json["orchestrator_admin_token"]  # 提取orc_token
            self.config.write_token("orc_token", orc_token)  # 把orc_token写入配置文件
            self.log.info("重新获取orc_admin_token成功")
        else:
            self.log.error("重新获取orc_admin_token失败")


if __name__ == "__main__":
    unittest.main()
