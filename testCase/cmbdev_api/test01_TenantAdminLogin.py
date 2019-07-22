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
        self.log.info(message="test01_cre_tenant", name="test06_CreateTenantAdmin.py", line=32)
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
        if dict_json["status"] == True:
            tenant_token = dict_json["tenant_admin_token"]  # 提取orc_token
            self.log.info(message="提取orc_token", name="test01_OrcLogin.py", line=42)
            self.log.info(message="%s" % tenant_token, name="test01_OrcLogin.py", line=42)
            authorization = "Bearer " + tenant_token
            self.json.write_data(authorization, "tenant_token_header", "Authorization")  # 把tenant_token写入json文件

        # 断言
        self.log.info(message="第三步：断言")
        self.assertEqual(status_code, 200, msg=">>>接口请求失败")
        self.assertTrue(dict_json["status"], msg=">>>断言失败，实际返回结果：%s" % dict_json)
        self.assertEqual(dict_json["username"], "auto_user", msg=">>>断言失败，实际返回值是：%s" % dict_json["username"])


if __name__ == "__main__":
    unittest.main()