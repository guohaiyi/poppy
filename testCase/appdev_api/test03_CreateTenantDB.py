#!/usr/bin/python3
# coding=utf-8
import json
import os
import unittest

from common.httpSet import HttpMethod
from common.myLog import MyLog
from common.readTestData import ReadTestData
from config.readConfig import ReadConfig

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
        self.log.info(message="----------测试开始----------", name="test01_OrcLogin.py")

    def tearDown(self):
        self.log.info(message="----------测试结束----------", name="test01_OrcLogin.py")

    def test01_get_db_list(self):
        """获取Tenant DB列表：Tenant DB列表为空"""
        self.log.info(message="test_login01", name="test03_CreateTenantDB.py", line=27)
        # 设置请求数据
        method = self.data.get_method(self.sheet, self.row[6])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[6])
        headers = self.hea_data.get_header(self.sheet, self.row[6])
        self.log.info(message="第一步: 获取请求数据")
        self.log.info(message="请求方法：%s" % method)
        self.log.info(message="url：%s" % url)

        # 发送请求
        status_code, res_json = self.http.http_method(method=method, url=url, headers=headers)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象
        self.log.info(message="第二步:发送请求，获取返回数据：")
        self.log.info(message="%s" % res_json)

        # 断言
        self.assertEqual(status_code, 200, msg=">>>test01_get_db_list接口请求失败")
        self.assertFalse(dict_json["status"], msg='>>>test01_get_db_list创建DB失败，实际返回结果：%s' % dict_json)
        self.assertEqual(dict_json["err"]["code"], 404,
                         msg=">>>test01_get_db_list断言失败，实际返回结果：%s" % dict_json["err"]["code"])
        self.assertEqual(dict_json["err"]["message"], "No records found",
                         msg=">>>test01_get_db_list断言失败，实际返回结果：%s" % dict_json["err"]["message"])

    def test02_create_db(self):
        """创建Tenant DB，不创建autolive"""
        self.log.info(message="test_login01", name="test03_CreateTenantDB.py", line=51)
        # 设置请求数据
        method = self.data.get_method(self.sheet, self.row[0])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[0])
        data = self.data.get_request_data(self.sheet, self.row[0])
        headers = self.hea_data.get_header(self.sheet, self.row[0])
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
        self.assertEqual(status_code, 200, msg=">>>test02_create_db接口请求失败")
        self.assertTrue(dict_json["status"], msg='>>>test02_create_db创建DB失败，实际返回结果：%s' % dict_json)

    def test03_create_db(self):
        """创建成功，并创建autolive"""
        self.log.info(message="test_login01", name="test03_CreateTenantDB.py", line=72)
        # 设置请求数据
        method = self.data.get_method(self.sheet, self.row[1])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[1])
        data = self.data.get_request_data(self.sheet, self.row[1])
        headers = self.hea_data.get_header(self.sheet, self.row[1])
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
        self.assertEqual(status_code, 200, msg=">>>test03_create_db接口请求失败")
        self.assertTrue(dict_json["status"], msg='>>>test03_create_db创建DB失败，实际返回结果：%s' % dict_json)

    def test04_create_db(self):
        """创建失败：缺少tenant name"""
        self.log.info(message="test_login01", name="test03_CreateTenantDB.py", line=93)
        # 设置请求数据
        method = self.data.get_method(self.sheet, self.row[2])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[2])
        data = self.data.get_request_data(self.sheet, self.row[2])
        headers = self.hea_data.get_header(self.sheet, self.row[2])
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
        self.assertEqual(status_code, 200, msg=">>>test04_create_db接口请求失败")
        self.assertFalse(dict_json["status"], msg=">>>test04_create_db断言失败，实际返回结果：%s" % dict_json)
        self.assertEqual(dict_json["err"]["code"], 400,
                         msg=">>>test04_create_db断言失败，实际返回结果：%s" % dict_json["err"]["code"])
        self.assertEqual(dict_json["err"]["message"], "Provide tenant name",
                         msg=">>>test04_create_db断言失败，实际返回结果：%s" % dict_json["err"]["message"])

    def test05_create_db(self):
        """创建失败：缺少db name"""
        self.log.info(message="test_login01", name="test03_CreateTenantDB.py", line=120)
        # 设置请求数据
        method = self.data.get_method(self.sheet, self.row[3])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[4])
        data = self.data.get_request_data(self.sheet, self.row[3])
        headers = self.hea_data.get_header(self.sheet, self.row[3])
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
        self.assertEqual(status_code, 200, msg=">>>test05_create_db接口请求失败")
        self.assertFalse(dict_json["status"], msg=">>>断言失败，实际返回结果：%s" % dict_json)
        self.assertEqual(dict_json["err"]["code"], 400, msg=">>>断言失败，实际返回结果：%s" % dict_json["err"]["code"])
        self.assertEqual(dict_json["err"]["message"], "Provide db",
                         msg=">>>断言失败，实际返回结果：%s" % dict_json["err"]["message"])

    def test06_create_db(self):
        """创建失败：tenant name已被占用"""
        self.log.info(message="test_login01", name="test03_CreateTenantDB.py", line=146)
        # 设置请求数据
        method = self.data.get_method(self.sheet, self.row[4])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[4])
        data = self.data.get_request_data(self.sheet, self.row[4])
        headers = self.hea_data.get_header(self.sheet, self.row[4])
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
        self.assertEqual(status_code, 200, msg=">>>test06_create_db接口请求失败")
        self.assertFalse(dict_json["status"], msg=">>>test06_create_db断言失败，实际返回结果：%s" % dict_json)
        self.assertEqual(dict_json["err"]["code"], 400,
                         msg=">>>test06_create_db断言失败，实际返回结果：%s" % dict_json["err"]["code"])
        self.assertEqual(dict_json["err"]["message"], "Tenant name/DB already exists",
                         msg=">>>test06_create_db断言失败，实际返回结果：%s" % dict_json["err"]["message"])

    def test07_create_db(self):
        """创建失败：db name已被占用"""
        self.log.info(message="test_login01", name="test03_CreateTenantDB.py", line=173)
        # 设置请求数据
        method = self.data.get_method(self.sheet, self.row[5])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[5])
        data = self.data.get_request_data(self.sheet, self.row[5])
        headers = self.hea_data.get_header(self.sheet, self.row[5])
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
        self.assertEqual(status_code, 200, msg=">>>test07_create_db接口请求失败")
        self.assertFalse(dict_json["status"], msg=">>>test07_create_db断言失败，实际返回结果：%s" % dict_json)
        self.assertEqual(dict_json["err"]["code"], 400,
                         msg=">>>test07_create_db断言失败，实际返回结果：%s" % dict_json["err"]["code"])
        self.assertEqual(dict_json["err"]["message"], "Tenant name/DB already exists",
                         msg=">>>test07_create_db断言失败，实际返回结果：%s" % dict_json["err"]["message"])

    def test08_get_db_list(self):
        """获取Tenant DB列表"""
        self.log.info(message="test_login01", name="test03_CreateTenantDB.py", line=200)
        # 设置请求数据
        method = self.data.get_method(self.sheet, self.row[7])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[7])
        headers = self.hea_data.get_header(self.sheet, self.row[7])
        self.log.info(message="第一步: 获取请求数据")
        self.log.info(message="请求方法：%s" % method)
        self.log.info(message="url：%s" % url)

        # 发送请求
        status_code, res_json = self.http.http_method(method=method, url=url, headers=headers)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象
        self.log.info(message="第二步:发送请求，获取返回数据：")
        self.log.info(message="%s" % res_json)

        # 断言
        self.assertEqual(status_code, 200, msg=">>>test08_get_db_list接口请求失败")
        self.assertTrue(dict_json["status"], msg='test08_get_db_list创建DB失败，实际返回结果：%s' % dict_json)
        self.assertIn("_id", dict_json["results"][0], msg="_id不存在：%s" % dict_json["results"][0])
        self.assertIn('tenant_name', dict_json["results"][0])
        self.assertIn("db", dict_json["results"][0])
        self.assertIn('info', dict_json["results"][0])
        self.assertIn('active_status', dict_json["results"][0])
        self.assertEqual(dict_json["results"][0]["tenant_name"], "auto_user_tenant",
                         msg=">>>test08_get_db_list断言失败，实际返回结果：%s" % dict_json["results"][0]["tenant_name"])
        self.assertIn("_id", dict_json["results"][1])
        self.assertIn('tenant_name', dict_json["results"][1])
        self.assertIn("db", dict_json["results"][1])
        self.assertIn('info', dict_json["results"][1])
        self.assertIn('active_status', dict_json["results"][1])
        self.assertEqual(dict_json["results"][1]["tenant_name"], "test_autolive",
                         msg=">>>test08_get_db_list断言失败，实际返回结果：%s" % dict_json["results"][1]["tenant_name"])


if __name__ == "__main__":
    unittest.main()
