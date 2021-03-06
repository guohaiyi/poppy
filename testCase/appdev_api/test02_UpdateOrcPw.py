#!/usr/bin/python3
# coding=utf-8
import json
import os
import unittest

from common.httpSet import HttpMethod
from common.myLog import MyLog
from common.operationJson import OperationJson
from common.readTestData import ReadTestData
from config.readConfig import ReadConfig

proDir = os.path.split(os.path.realpath(__file__))[0]
file_name = os.path.join(proDir, "../../testDataFile/orchestrator_account.json")


class TestUpdateOrcPw(unittest.TestCase):
    def setUp(self) -> None:
        self.data = ReadTestData(file_name)
        self.hea_data = ReadTestData()
        self.log = MyLog()
        self.config = ReadConfig()
        self.http = HttpMethod()
        self.json = OperationJson()
        self.sheet = "app_test_case"
        self.row = [7, 8, 9, 10, 11]
        self.log.info(message="----------测试开始----------", name="test02_UpdateOrcPw.py")

    def tearDown(self) -> None:
        self.log.info(message="----------测试结束----------", name="test02_UpdateOrcPw.py")

    def test_update01(self):
        """更新密码失败：旧密码错误"""
        self.log.info(message="test_update01", name="test02_UpdateOrcPw.py", line=34)
        # 配置请求数据
        method = self.data.get_method(self.sheet, self.row[0])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[0])
        headers = self.hea_data.get_header(self.sheet, self.row[0])
        data = self.data.get_request_data(self.sheet, self.row[0])
        self.log.info(message="第一步: 获取请求数据")
        self.log.info(message="请求方法：%s" % method)
        self.log.info(message="url：%s" % url)
        self.log.info(message="请求数据：%s" % data)

        # 发送请求
        status_code, res_json = self.http.http_method(method=method, url=url, headers=headers, data=data)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象

        # 断言
        self.assertEqual(status_code, 200, msg=">>>test_update01接口请求失败")
        self.assertFalse(dict_json["status"], msg=">>>test_update01断言失败，实际返回结果：%s" % dict_json)
        self.assertEqual(dict_json["err"]["code"], 400, msg=">>>test_update01断言失败，实际返回值是：%s" % dict_json["err"]["code"])
        self.assertEqual(dict_json["err"]["message"], "Username or password error",
                         msg=">>>test_update01断言失败，实际返回值是：%s" % dict_json["err"]["message"])

    def test_update02(self):
        """更新密码失败：username不存在"""
        self.log.info(message="test_update02", name="test02_UpdateOrcPw.py", line=58)
        # 配置请求数据
        method = self.data.get_method(self.sheet, self.row[1])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[1])
        headers = self.hea_data.get_header(self.sheet, self.row[1])
        data = self.data.get_request_data(self.sheet, self.row[1])
        self.log.info(message="第一步: 获取请求数据")
        self.log.info(message="请求方法：%s" % method)
        self.log.info(message="url：%s" % url)
        self.log.info(message="请求数据：%s" % data)

        # 发送请求
        status_code, res_json = self.http.http_method(method=method, url=url, headers=headers, data=data)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象

        # 断言
        self.assertEqual(status_code, 200, msg=">>>接口请求失败")
        self.assertFalse(dict_json["status"], msg=">>>断言失败，实际返回结果：%s" % dict_json)
        self.assertEqual(dict_json["err"]["code"], 404, msg=">>>断言失败，实际返回值是：%s" % dict_json["err"]["code"])
        self.assertEqual(dict_json["err"]["message"], "Username does not exists",
                         msg=">>>断言失败，实际返回值是：%s" % dict_json["err"]["message"])

    def test_update03(self):
        """更新密码失败：缺少new_password字段"""
        self.log.info(message="test_update03", name="test02_UpdateOrcPw.py", line=82)
        # 配置请求数据
        method = self.data.get_method(self.sheet, self.row[2])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[2])
        headers = self.hea_data.get_header(self.sheet, self.row[2])
        data = self.data.get_request_data(self.sheet, self.row[2])
        self.log.info(message="第一步: 获取请求数据")
        self.log.info(message="请求方法：%s" % method)
        self.log.info(message="url：%s" % url)
        self.log.info(message="请求数据：%s" % data)

        # 发送请求
        status_code, res_json = self.http.http_method(method=method, url=url, headers=headers, data=data)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象

        # 断言
        self.assertEqual(status_code, 200, msg=">>>接口请求失败")
        self.assertFalse(dict_json["status"], msg=">>>断言失败，实际返回结果：%s" % dict_json)
        self.assertEqual(dict_json["err"]["code"], 400, msg=">>>断言失败，实际返回值是：%s" % dict_json["err"]["code"])
        self.assertEqual(dict_json["err"]["message"], "New password is needed",
                         msg=">>>断言失败，实际返回值是：%s" % dict_json["err"]["message"])

    def test_update04(self):
        """更新密码失败：缺少current_password字段"""
        self.log.info(message="test_update04", name="test02_UpdateOrcPw.py", line=106)
        # 配置请求数据
        method = self.data.get_method(self.sheet, self.row[3])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[3])
        headers = self.hea_data.get_header(self.sheet, self.row[3])
        data = self.data.get_request_data(self.sheet, self.row[3])
        self.log.info(message="第一步: 获取请求数据")
        self.log.info(message="请求方法：%s" % method)
        self.log.info(message="url：%s" % url)
        self.log.info(message="请求数据：%s" % data)

        # 发送请求
        status_code, res_json = self.http.http_method(method=method, url=url, headers=headers, data=data)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象

        # 断言
        self.assertEqual(status_code, 200, msg=">>>接口请求失败")
        self.assertFalse(dict_json["status"], msg=">>>断言失败，实际返回结果：%s" % dict_json)
        self.assertEqual(dict_json["err"]["code"], 400, msg=">>>断言失败，实际返回值是：%s" % dict_json["err"]["code"])
        self.assertEqual(dict_json["err"]["message"], "Current password is needed",
                         msg=">>>断言失败，实际返回值是：%s" % dict_json["err"]["message"])

    def test_update05(self):
        """更新密码成功"""
        self.log.info(message="test_update05", name="test02_UpdateOrcPw.py", line=130)
        # 配置请求数据
        method = self.data.get_method(self.sheet, self.row[4])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[4])
        headers = self.hea_data.get_header(self.sheet, self.row[4])
        data = self.data.get_request_data(self.sheet, self.row[4])
        self.log.info(message="第一步: 获取请求数据")
        self.log.info(message="请求方法：%s" % method)
        self.log.info(message="url：%s" % url)
        self.log.info(message="请求数据：%s" % data)

        # 发送请求
        status_code, res_json = self.http.http_method(method=method, url=url, headers=headers, data=data)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象

        # 断言
        self.assertEqual(status_code, 200, msg=">>>接口请求失败")
        self.assertTrue(dict_json["status"], msg=">>>断言失败，实际返回结果：%s" % dict_json)

        # 密码成功重新获取orc_token
        if dict_json["status"] == True:
            self.check_new_login()
        else:
            self.log.error("Orc Admin密码更新失败")

    def check_new_login(self):
        """重新获取orc_admin_token"""
        # 获取测试数据
        method = self.data.get_method(self.sheet, 2)
        url = self.config.get_base_url() + self.data.get_url(self.sheet, 2)
        data = self.data.get_rely_data(self.sheet, self.row[4])
        headers = self.hea_data.get_header(self.sheet, self.row[2])

        # 发送请求
        status_code, res_json = self.http.http_method(method=method, url=url, data=data, headers=headers)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象
        if dict_json["status"]:
            orc_token = dict_json["orchestrator_admin_token"]  # 提取orc_token
            authorization = "Bearer " + orc_token
            self.json.write_data(authorization, "orc_token_header", "Authorization")  # 把orc_token写入json文件
            self.log.info("check_new_login重新获取orc_admin_token成功", "check_new_login", 170)
            self.restore_orc_pw()  # 调用还原密码
        else:
            self.log.error("check_new_login重新获取orc_admin_token失败", "check_new_login", 173)

    def restore_orc_pw(self):
        """还原密码"""
        # 配置请求数据
        method = self.data.get_method(self.sheet, self.row[4])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[4])
        headers = self.hea_data.get_header(self.sheet, self.row[4])
        data = self.data.get_request_data(self.sheet, self.row[0])

        # 发送请求
        status_code, res_json = self.http.http_method(method=method, url=url, headers=headers, data=data)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象
        if dict_json["status"]:
            self.log.info("restore_orc_pw orc admin密码还原成功", "restore_orc_pw", 187)
            self.restore_get_pw()
        else:
            self.log.error("restore_orc_pw orc admin密码还原失败""restore_orc_pw", 190)

    def restore_get_pw(self):
        """还原密码之后重新获取orc_token"""
        # 获取测试数据
        method = self.data.get_method(self.sheet, 2)
        url = self.config.get_base_url() + self.data.get_url(self.sheet, 2)
        headers = self.hea_data.get_header(self.sheet, 2)
        data = self.data.get_request_data(self.sheet, 2)

        # 发送请求
        status_code, res_json = self.http.http_method(method=method, url=url, data=data, headers=headers)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象
        if dict_json["status"]:
            orc_token = dict_json["orchestrator_admin_token"]  # 提取orc_token
            authorization = "Bearer " + orc_token
            self.json.write_data(authorization, "orc_token_header", "Authorization")  # 把orc_token写入json文件
            self.log.info("还原密码之后重新获取orc_token成功""restore_get_pw", 207)
        else:
            self.log.error("还原密码之后重新获取orc_token失败""restore_get_pw", 209)


if __name__ == "__main__":
    unittest.main()
