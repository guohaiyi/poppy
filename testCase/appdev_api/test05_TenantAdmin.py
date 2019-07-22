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
        self.sheet = 'app_test_case'
        self.row = [30, 31, 32, 33, 34, 35, 36, 37, 38, 39]
        self.log.info(message="----------测试开始----------", name="test06_TenantAdmin.py")

    def tearDown(self):
        self.log.info(message="----------测试结束----------", name="test06_TenantAdmin.py")

    def test01_get_tenant_admin_list(self):
        """获取Tenant Admin列表：为空"""
        self.log.info(message="test01_get_tenant_admin_list", name="test06_TenantAdmin.py", line=35)
        # 获取测试数据
        method = self.data.get_method(self.sheet, self.row[0])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[0])
        headers = self.hea_data.get_header(self.sheet, self.row[0])
        self.log.info(message="第一步: 获取请求数据")
        self.log.info(message="请求方法：%s" % method)
        self.log.info(message="url：%s" % url)

        # 发送请求
        status_code, res_json = self.http.http_method(method=method, url=url, headers=headers)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象
        self.log.info(message="第二步:发送请求，获取返回数据：")
        self.log.info(message="%s" % res_json)

        # 断言
        self.log.info(message="第三步：断言")
        self.assertEqual(status_code, 200, msg=">>>接口请求失败")
        self.assertFalse(dict_json["status"], msg=">>>断言失败，实际返回结果：%s" % dict_json)
        self.assertEqual(dict_json["err"]["code"], 404, msg='>>>断言失败，实际返回结果：%s' % dict_json["err"]["code"])
        self.assertEqual(dict_json["err"]["message"], "No records found",
                         msg='>>>断言失败，实际返回结果：%s' % dict_json["err"]["message"])

    def test02_get_tenant_admin_info(self):
        """获取Tenant Admin信息：不存在"""
        self.log.info(message="test02_get_tenant_admin_info", name="test06_TenantAdmin.py", line=60)
        # 获取测试数据
        method = self.data.get_method(self.sheet, self.row[1])
        data = self.data.get_param(self.sheet, self.row[1])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[1]) + data
        headers = self.hea_data.get_header(self.sheet, self.row[1])
        self.log.info(message="第一步: 获取请求数据")
        self.log.info(message="请求方法：%s" % method)
        self.log.info(message="url：%s" % url)

        # 发送请求
        status_code, res_json = self.http.http_method(method=method, url=url, headers=headers)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象
        self.log.info(message="第二步:发送请求，获取返回数据：")
        self.log.info(message="%s" % res_json)

        # 断言
        self.log.info(message="第三步：断言")
        self.assertEqual(status_code, 200, msg=">>>接口请求失败")
        self.assertFalse(dict_json["status"], msg=">>>断言失败，实际返回结果：%s" % dict_json)
        self.assertEqual(dict_json["err"]["code"], 404, msg='>>>断言失败，实际返回结果：%s' % dict_json["err"]["code"])
        self.assertEqual(dict_json["err"]["message"], "No tenant_admin exist with matching ID",
                         msg='>>>断言失败，实际返回结果：%s' % dict_json["err"]["message"])

    def test03_cre_tenant_admin(self):
        """创建Tenant Admin"""
        self.log.info(message="test03_cre_tenant_admin", name="test06_TenantAdmin.py", line=86)
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
        self.assertTrue(dict_json["status"], msg=">>>断言失败，实际返回结果：%s" % dict_json)
        self.assertEqual(dict_json["username"], "auto_user",
                         msg=">>>断言失败，实际返回值是：%s" % dict_json["username"])

    def test04_cre_tenant_admin(self):
        """创建失败：缺失username"""
        self.log.info(message="test04_cre_tenant_admin", name="test06_TenantAdmin.py", line=112)
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
        self.assertEqual(dict_json["err"]["message"], "Username is needed",
                         msg='>>>断言失败，实际返回结果：%s' % dict_json["err"]["message"])

    def test05_cre_tenant_admin(self):
        """创建失败：缺失password"""
        self.log.info(message="test05_cre_tenant_admin", name="test06_TenantAdmin.py", line=139)
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
        self.assertEqual(dict_json["err"]["message"], "Password is needed",
                         msg='>>>断言失败，实际返回结果：%s' % dict_json["err"]["message"])

    def test06_cre_tenant_admin(self):
        """创建失败：缺失password"""
        self.log.info(message="test06_cre_tenant_admin", name="test06_TenantAdmin.py", line=166)
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
        self.assertEqual(dict_json["err"]["message"], "Tenant name is needed",
                         msg='>>>断言失败，实际返回结果：%s' % dict_json["err"]["message"])

    def test07_cre_tenant_admin(self):
        """创建失败：缺失password"""
        self.log.info(message="test07_cre_tenant_admin", name="test06_TenantAdmin.py", line=193)
        # 获取测试数据
        method = self.data.get_method(self.sheet, self.row[6])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[6])
        headers = self.hea_data.get_header(self.sheet, self.row[6])
        data = self.data.get_request_data(self.sheet, self.row[6])
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
        self.assertEqual(dict_json["err"]["message"], "Username not available for this tenant. Try another username.",
                         msg='>>>断言失败，实际返回结果：%s' % dict_json["err"]["message"])

    def test08_cre_tenant_admin(self):
        """创建失败：缺失password"""
        self.log.info(message="test08_cre_tenant_admin", name="test06_TenantAdmin.py", line=220)
        # 获取测试数据
        method = self.data.get_method(self.sheet, self.row[7])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[7])
        headers = self.hea_data.get_header(self.sheet, self.row[7])
        data = self.data.get_request_data(self.sheet, self.row[7])
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
        self.assertEqual(dict_json["err"]["code"], 404, msg='>>>断言失败，实际返回结果：%s' % dict_json["err"]["code"])
        self.assertEqual(dict_json["err"]["message"], "Tenant doesn't exist",
                         msg='>>>断言失败，实际返回结果：%s' % dict_json["err"]["message"])

    def test09_get_tenant_admin_list(self):
        """获取所有Tenant Admin列表"""
        self.log.info(message="test09_get_tenant_admin_list", name="test06_TenantAdmin.py", line=247)
        # 获取测试数据
        method = self.data.get_method(self.sheet, self.row[8])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[8])
        headers = self.hea_data.get_header(self.sheet, self.row[8])
        self.log.info(message="第一步: 获取请求数据")
        self.log.info(message="请求方法：%s" % method)
        self.log.info(message="url：%s" % url)

        # 发送请求
        status_code, res_json = self.http.http_method(method=method, url=url, headers=headers)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象
        self.log.info(message="第二步:发送请求，获取返回数据：")
        self.log.info(message="%s" % res_json)

        # 断言
        self.log.info(message="第三步：断言")
        self.assertEqual(status_code, 200, msg=">>>接口请求失败")
        self.assertTrue(dict_json["status"], msg=">>>断言失败，实际返回结果：%s" % dict_json)
        exist_key = ["_id", "username", "tenant_name", "active_status", "created_time", "updated_time"]
        for key in exist_key:
            self.assertIn(key, dict_json["results"][0], msg=">>>返回数据里面没有该字段：%s" % key)
        self.assertEqual(dict_json["results"][0]["username"], "auto_user")
        self.assertEqual(dict_json["results"][0]["tenant_name"], "auto_tenant_name")
        self.assertTrue(dict_json["results"][0]["username"])

    def test10_get_tenant_admin_info(self):
        """获取Tenant Admin信息"""
        self.log.info(message="test10_get_tenant_admin_info", name="test06_TenantAdmin.py", line=274)
        # 获取测试数据
        method = self.data.get_method(self.sheet, self.row[9])
        data = self.data.get_param(self.sheet, self.row[9])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[9]) + data
        headers = self.hea_data.get_header(self.sheet, self.row[9])
        self.log.info(message="第一步: 获取请求数据")
        self.log.info(message="请求方法：%s" % method)
        self.log.info(message="url：%s" % url)

        # 发送请求
        status_code, res_json = self.http.http_method(method=method, url=url, headers=headers)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象
        self.log.info(message="第二步:发送请求，获取返回数据：")
        self.log.info(message="%s" % res_json)

        # 断言
        self.log.info(message="第三步：断言")
        self.assertEqual(status_code, 200, msg=">>>接口请求失败")
        self.assertTrue(dict_json["status"], msg=">>>断言失败，实际返回结果：%s" % dict_json)
        exist_key = ["_id", "username", "tenant_name", "active_status", "created_time", "updated_time"]
        for key in exist_key:
            self.assertIn(key, dict_json, msg=">>>返回数据里面没有该字段：%s" % key)
        self.assertEqual(dict_json["username"], "auto_user")
        self.assertEqual(dict_json["tenant_name"], "auto_tenant_name")
        self.assertTrue(dict_json["username"])


if __name__ == "__main__":
    unittest.main()
