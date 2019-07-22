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
file_name = os.path.join(proDir, "../../testDataFile/tenant_account.json")
print('file_name:%s' % file_name)


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.data = ReadTestData(file_name)
        self.hea_data = ReadTestData()
        self.http = HttpMethod()
        self.config = ReadConfig()
        self.log = MyLog()
        self.json = OperationJson()
        self.sheet = 'cmb_test_case'
        self.row = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        self.log.info(message="----------测试开始----------", name="test01_TenantAdminLogin.py")

    def tearDown(self):
        self.log.info(message="----------测试结束----------", name="test01_TenantAdminLogin.py")

    def test01_admin_login(self):
        """Tenant admin正常登录"""
        self.log.info(message="test01_admin_login", name="test01_TenantAdminLogin.py", line=35)
        # 获取测试数据
        method = self.data.get_method(self.sheet, self.row[0])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[0])
        headers = self.hea_data.get_header(self.sheet, self.row[0])
        data = self.data.get_request_data(self.sheet, self.row[0])
        self.log.info(message="第一步: 获取请求数据")
        self.log.info(message="请求方法：%s" % method)
        self.log.info(message="url：%s" % url)
        self.log.info(message="请求数据：%s" % data)

        # 发送请求
        status_code, res_json = self.http.http_method(method=method, url=url, data=data, headers=headers)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象
        self.log.info(message="第二步:发送请求，获取返回数据：")
        self.log.info(message="%s" % res_json)
        if dict_json["status"]:
            tenant_token = dict_json["tenant_admin_token"]  # 提取tenant_admin_token
            self.log.info(message="提取tenant_admin_token：")
            self.log.info(message="%s" % tenant_token)
            authorization = "Bearer " + tenant_token
            self.json.write_data(authorization, "tenant_token_header", "Authorization")  # 把tenant_admin_token写入json文件

        # 断言
        self.log.info(message="第三步：断言")
        self.assertEqual(status_code, 200, msg=">>>接口请求失败")
        self.assertTrue(dict_json["status"], msg=">>>断言失败，实际返回结果：%s" % dict_json)
        self.assertEqual(dict_json["username"], "auto_user", msg=">>>断言失败，实际返回值是：%s" % dict_json["username"])

    def test02_admin_login(self):
        """登录失败：密码错误"""
        self.log.info(message="test02_admin_login", name="test05_TenantAdmin.py", line=32)
        # 获取测试数据
        method = self.data.get_method(self.sheet, self.row[1])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[1])
        headers = self.hea_data.get_header(self.sheet, self.row[1])
        data = self.data.get_request_data(self.sheet, self.row[1])
        self.log.info(message="第一步: 获取请求数据")
        self.log.info(message="请求方法：%s" % method)
        self.log.info(message="url：%s" % url)
        self.log.info(message="请求数据：%s" % data)

        # 发送请求
        status_code, res_json = self.http.http_method(method=method, url=url, data=data, headers=headers)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象
        self.log.info(message="第二步:发送请求，获取返回数据：")
        self.log.info(message="%s" % res_json)

        # 断言
        self.log.info(message="第三步：断言")
        self.assertEqual(status_code, 200, msg=">>>接口请求失败")
        self.assertFalse(dict_json["status"], msg=">>>断言失败，实际返回结果：%s" % dict_json)
        self.assertEqual(dict_json["err"]["code"], 400, msg='>>>断言失败，实际返回结果：%s' % dict_json["err"]["code"])
        self.assertEqual(dict_json["err"]["message"], "Username or password error.",
                         msg='>>>断言失败，实际返回结果：%s' % dict_json["err"]["message"])

    def test03_admin_login(self):
        """登录失败：缺少username"""
        self.log.info(message="test02_admin_login", name="test05_TenantAdmin.py", line=32)
        # 获取测试数据
        method = self.data.get_method(self.sheet, self.row[2])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[2])
        headers = self.hea_data.get_header(self.sheet, self.row[2])
        data = self.data.get_request_data(self.sheet, self.row[2])
        self.log.info(message="第一步: 获取请求数据")
        self.log.info(message="请求方法：%s" % method)
        self.log.info(message="url：%s" % url)
        self.log.info(message="请求数据：%s" % data)

        # 发送请求
        status_code, res_json = self.http.http_method(method=method, url=url, data=data, headers=headers)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象
        self.log.info(message="第二步:发送请求，获取返回数据：")
        self.log.info(message="%s" % res_json)

        # 断言
        self.log.info(message="第三步：断言")
        self.assertEqual(status_code, 200, msg=">>>接口请求失败")
        self.assertFalse(dict_json["status"], msg=">>>断言失败，实际返回结果：%s" % dict_json)
        self.assertEqual(dict_json["err"]["code"], 400, msg='>>>断言失败，实际返回结果：%s' % dict_json["err"]["code"])
        self.assertEqual(dict_json["err"]["message"], "Username is needed",
                         msg='>>>断言失败，实际返回结果：%s' % dict_json["err"]["message"])

    def test04_admin_login(self):
        """登录失败：缺少password"""
        self.log.info(message="test02_admin_login", name="test05_TenantAdmin.py", line=32)
        # 获取测试数据
        method = self.data.get_method(self.sheet, self.row[3])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[3])
        headers = self.hea_data.get_header(self.sheet, self.row[3])
        data = self.data.get_request_data(self.sheet, self.row[3])
        self.log.info(message="第一步: 获取请求数据")
        self.log.info(message="请求方法：%s" % method)
        self.log.info(message="url：%s" % url)
        self.log.info(message="请求数据：%s" % data)

        # 发送请求
        status_code, res_json = self.http.http_method(method=method, url=url, data=data, headers=headers)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象
        self.log.info(message="第二步:发送请求，获取返回数据：")
        self.log.info(message="%s" % res_json)

        # 断言
        self.log.info(message="第三步：断言")
        self.assertEqual(status_code, 200, msg=">>>接口请求失败")
        self.assertFalse(dict_json["status"], msg=">>>断言失败，实际返回结果：%s" % dict_json)
        self.assertEqual(dict_json["err"]["code"], 400, msg='>>>断言失败，实际返回结果：%s' % dict_json["err"]["code"])
        self.assertEqual(dict_json["err"]["message"], "Password is needed",
                         msg='>>>断言失败，实际返回结果：%s' % dict_json["err"]["message"])

    def test05_admin_login(self):
        """登录失败：缺少tenant_name"""
        self.log.info(message="test02_admin_login", name="test05_TenantAdmin.py", line=32)
        # 获取测试数据
        method = self.data.get_method(self.sheet, self.row[4])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[4])
        headers = self.hea_data.get_header(self.sheet, self.row[4])
        data = self.data.get_request_data(self.sheet, self.row[4])
        self.log.info(message="第一步: 获取请求数据")
        self.log.info(message="请求方法：%s" % method)
        self.log.info(message="url：%s" % url)
        self.log.info(message="请求数据：%s" % data)

        # 发送请求
        status_code, res_json = self.http.http_method(method=method, url=url, data=data, headers=headers)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象
        self.log.info(message="第二步:发送请求，获取返回数据：")
        self.log.info(message="%s" % res_json)

        # 断言
        self.log.info(message="第三步：断言")
        self.assertEqual(status_code, 200, msg=">>>接口请求失败")
        self.assertFalse(dict_json["status"], msg=">>>断言失败，实际返回结果：%s" % dict_json)
        self.assertEqual(dict_json["err"]["code"], 400, msg='>>>断言失败，实际返回结果：%s' % dict_json["err"]["code"])
        self.assertEqual(dict_json["err"]["message"], "Tenant name is needed",
                         msg='>>>断言失败，实际返回结果：%s' % dict_json["err"]["message"])

    def test06_admin_login(self):
        """登录失败：缺少tenant_name"""
        self.log.info(message="test02_admin_login", name="test05_TenantAdmin.py", line=32)
        # 获取测试数据
        method = self.data.get_method(self.sheet, self.row[5])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[5])
        headers = self.hea_data.get_header(self.sheet, self.row[5])
        data = self.data.get_request_data(self.sheet, self.row[5])
        self.log.info(message="第一步: 获取请求数据")
        self.log.info(message="请求方法：%s" % method)
        self.log.info(message="url：%s" % url)
        self.log.info(message="请求数据：%s" % data)

        # 发送请求
        status_code, res_json = self.http.http_method(method=method, url=url, data=data, headers=headers)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象
        self.log.info(message="第二步:发送请求，获取返回数据：")
        self.log.info(message="%s" % res_json)

        # 断言
        self.log.info(message="第三步：断言")
        self.assertEqual(status_code, 200, msg=">>>接口请求失败")
        self.assertFalse(dict_json["status"], msg=">>>断言失败，实际返回结果：%s" % dict_json)
        self.assertEqual(dict_json["err"]["code"], 400, msg='>>>断言失败，实际返回结果：%s' % dict_json["err"]["code"])
        self.assertEqual(dict_json["err"]["message"],  "Username/tenant_name error.",
                         msg='>>>断言失败，实际返回结果：%s' % dict_json["err"]["message"])


if __name__ == "__main__":
    unittest.main()
