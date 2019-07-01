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
file_name = os.path.join(proDir, "../testDataFile/tenant_db.json")


class CreateTenantDbTest(unittest.TestCase):
    def setUp(self):
        self.data = ReadData(file_name)
        self.http = HttpMethod()
        self.config = ReadConfig()
        self.log = MyLog()
        self.oper_excel = OperationExcel()

    def test_create_success(self):
        """创建Tenant DB，不创建autolive"""
        line = 7
        case_id = self.data.get_case_id(line)
        case_title = self.data.get_case_title(line)
        method = self.data.get_method(line)
        url = self.config.get_base_url() + self.data.get_url(line)
        data = self.data.get_request_data(line)
        headers = {"Content-Type": "application/json", "Authorization": "Bearer " + self.config.get_token('orc_token')}
        status_code, res_json = self.http.http_method(method=method, url=url, data=data, headers=headers)
        self.oper_excel.write_data('K', line, res_json)  # 把实际返回结果写入Excel
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象
        # 断言
        self.assertEqual(status_code, 200, msg="两个值不相等")
        self.assertTrue(dict_json["status"], msg='>>>创建DB失败，实际返回结果：%s' % dict_json)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
