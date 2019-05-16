# -*- coding: UTF-8 -*-
import unittest
import json
from common.readData import ReadData
from common.httpSet import HttpMethod
from config.readConfig import ReadConfig
from common.myLog import MyLog
from common.operationExcel import OperationExcel

file_name = "../testDataFile/orchestrator_account.json"


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.data = ReadData(file_name)
        self.http = HttpMethod()
        self.config = ReadConfig()
        self.log = MyLog()
        self.oper_excel = OperationExcel()

    def test_login_success(self):
        method = self.data.get_method(2)
        url = self.config.get_base_url() + self.data.get_url(2)
        data = self.data.get_request_data(2)
        headers = {"Content-Type": "application/json"}
        status_code, res_json = self.http.http_method(method=method, url=url, data=data, headers=headers)
        self.oper_excel.write_data('K', 2, res_json)  # 把实际返回结果写入Excel
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象
        print(status_code)
        try:
            self.assertTrue(dict_json["status"])
            self.assertEqual(dict_json["username"], "orc_admin")
            self.log.info("测试通过")
            self.oper_excel.write_data('J', 2, 'PASS')
            orc_token = dict_json["orchestrator_admin_token"]
            self.config.write_orc_token(orc_token)  # 把orc_token写入配置文件
        except Exception as e:
            self.log.error("测试失败：%s" % e)
            print("测试失败")
            self.oper_excel.write_data('J', 2, 'FAIL')


def test_login_fail(self):
    method = self.data.get_method(3)
    url = self.config.get_base_url() + self.data.get_url(3)
    data = self.data.get_request_data(3)
    headers = self.data.get_headers(3)
    try:
        res = self.http.http_method(method=method, url=url, data=data, headers=headers)
        dict_json = json.loads(res)  # 把json数据转换成字典对象
        self.assertFalse(dict_json["status"])
        self.assertEqual(dict_json["err"]["code"], 400)
        self.assertEqual(dict_json["err"]["message"], "Username or password error")
        self.log.info("测试通过")
    except Exception as e:
        self.log.error(e)


def tearDown(self):
    pass


if __name__ == "__main__":
    unittest.main()
