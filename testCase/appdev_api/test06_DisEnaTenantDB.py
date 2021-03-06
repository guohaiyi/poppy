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
        self.row = [36, 37, 38, 39]
        self.log.info(message="----------测试开始----------", name="test06_DisEnaTenantDB.py")

    def tearDown(self):
        self.log.info(message="----------测试结束----------", name="test06_DisEnaTenantDB.py")

    def test01_DisTenDb(self):
        """禁用TenantDB"""
        self.log.info(message="test01_DisTenDb", name="test06_DisEnaTenantDB.py", line=32)
        # 设置请求数据
        method = self.data.get_method(self.sheet, self.row[0])
        data = self.data.get_param(self.sheet, self.row[0])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[0]) + data
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
        self.assertTrue(dict_json["status"], msg='>>>禁用DB失败，实际返回结果：%s' % dict_json)

        # 检查是否成功禁用
        if dict_json["status"]:
            return_data = self.check_is_success()
            self.assertFalse(return_data["status"], msg='>>>禁用TenantDB验证不通过')
            self.assertEqual(return_data["err"]["code"], 403,
                             msg='>>>禁用TenantDB验证不通过，实际返回结果：%s' % return_data["err"]["code"])
            self.assertEqual(return_data["err"]["message"], "This Account is blocked.",
                             msg='>>>禁用TenantDB验证不通过，实际返回结果：%s' % return_data["err"]["message"])

    def test02_DisTenDbFail(self):
        """禁用TenantDB失败：不存在"""
        self.log.info(message="test02_DisTenDbFail", name="test06_DisEnaTenantDB.py", line=32)
        # 设置请求数据
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
        self.assertFalse(dict_json["status"], msg='>>>禁用DB失败，实际返回结果：%s' % dict_json)
        self.assertEqual(dict_json["err"]["code"], 404, msg='>>>禁用DB失败，实际返回结果：%s' % dict_json["err"]["code"])
        self.assertEqual(dict_json["err"]["message"], "No record exist for given ID",
                         msg='>>>禁用DB失败，实际返回结果：%s' % dict_json["err"]["message"])

    def test03_EnaTenDb(self):
        """启用TenantDB"""
        self.log.info(message="test03_EnaTenDb", name="test06_DisEnaTenantDB.py", line=32)
        # 设置请求数据
        method = self.data.get_method(self.sheet, self.row[2])
        data = self.data.get_param(self.sheet, self.row[2])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[2]) + data
        headers = self.hea_data.get_header(self.sheet, self.row[2])
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
        self.assertTrue(dict_json["status"], msg='>>>启用DB失败，实际返回结果：%s' % dict_json)

        # 检查是否成功启用TenantDB
        if dict_json["status"]:
            return_data = self.check_is_success()
            self.assertTrue(return_data["status"], msg='>>>启用TenantDB验证不通过')

    def test04_TenDbFail(self):
        """启用TenantDB成功：不存在"""
        self.log.info(message="test04_TenDbFail", name="test06_DisEnaTenantDB.py", line=32)
        # 设置请求数据
        method = self.data.get_method(self.sheet, self.row[3])
        data = self.data.get_param(self.sheet, self.row[3])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[3]) + data
        headers = self.hea_data.get_header(self.sheet, self.row[3])
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
        self.assertFalse(dict_json["status"], msg='>>>禁用DB失败，实际返回结果：%s' % dict_json)
        self.assertEqual(dict_json["err"]["code"], 404, msg='>>>禁用DB失败，实际返回结果：%s' % dict_json["err"]["code"])
        self.assertEqual(dict_json["err"]["message"], "No record exist for given ID",
                         msg='>>>禁用DB失败，实际返回结果：%s' % dict_json["err"]["message"])

    def check_is_success(self):
        """通过登录Tenant Admin来验证Tenant DB是否禁用或启用成功"""
        file = os.path.join(proDir, "../../testDataFile/tenant_account.json")
        data = ReadTestData(file)
        sheet = "cmb_test_case"
        row = 2
        method = data.get_method(sheet, row)
        url = self.config.get_base_url() + data.get_url(sheet, row)
        headers = self.hea_data.get_header(sheet, row)
        data = data.get_request_data(sheet, row)

        # 发送请求
        status_code, res_json = self.http.http_method(method=method, url=url, data=data, headers=headers)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象
        return dict_json


if __name__ == "__main__":
    unittest.main()
