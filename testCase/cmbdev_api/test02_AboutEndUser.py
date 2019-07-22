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
file_name = os.path.join(proDir, "../../testDataFile/end_user.json")
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
        self.row = [8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
        self.log.info(message="----------测试开始----------", name="test02_AboutEndUser.py")

    def tearDown(self):
        self.log.info(message="----------测试结束----------", name="test02_AboutEndUser.py")

    def test01_get_user_list(self):
        """用户不存在：列表为空"""
        self.log.info(message="test01_get_user_list", name="test02_AboutEndUser.py", line=35)
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
        self.assertEqual(dict_json["err"]["message"], "No records exist",
                         msg='>>>断言失败，实际返回结果：%s' % dict_json["err"]["message"])

    def test02_cre_user(self):
        """创建用户"""
        self.log.info(message="test02_cre_user", name="test02_AboutEndUser.py", line=60)
        # 获取测试数据
        method = self.data.get_method(self.sheet, self.row[1])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[1])
        headers = self.hea_data.get_header(self.sheet, self.row[1])
        data1 = self.data.get_request_data(self.sheet, self.row[1])
        data2 = self.data.get_param(self.sheet, self.row[1])
        self.log.info(message="第一步: 获取请求数据")
        self.log.info(message="请求方法：%s" % method)
        self.log.info(message="url：%s" % url)
        self.log.info(message="请求数据：%s" % data1)

        # 创建2个用户
        for data_key in [data1, data2]:
            # 发送请求
            status_code, res_json = self.http.http_method(method=method, url=url, data=data_key, headers=headers)
            dict_json = json.loads(res_json)  # 把json数据转换成字典对象
            self.log.info(message="第二步:发送请求，获取返回数据：")
            self.log.info(message="%s" % res_json)

            # 断言
            self.log.info(message="第三步：断言")
            self.assertEqual(status_code, 200, msg=">>>接口请求失败")
            self.assertTrue(dict_json["status"], msg=">>>断言失败，实际返回结果：%s" % dict_json)

    def test03_cre_user(self):
        """创建用户失败：user_id被占用"""
        self.log.info(message="test03_cre_user", name="test02_AboutEndUser.py", line=87)
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
        self.assertEqual(dict_json["err"]["message"], "user_id already exists",
                         msg='>>>断言失败，实际返回结果：%s' % dict_json["err"]["message"])

    def test04_cre_user(self):
        """创建用户失败：不传入user_id"""
        self.log.info(message="test04_cre_user", name="test02_AboutEndUser.py", line=114)
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
        self.assertEqual(dict_json["err"]["message"], "user_id is mandatory",
                         msg='>>>断言失败，实际返回结果：%s' % dict_json["err"]["message"])

    def test05_get_user_list(self):
        """用户存在：返回所有用户列表"""
        self.log.info(message="test05_get_user_list", name="test02_AboutEndUser.py", line=141)
        # 获取测试数据
        method = self.data.get_method(self.sheet, self.row[4])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[4])
        headers = self.hea_data.get_header(self.sheet, self.row[4])
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
        for key in ["results", "previous", "hasPrevious", "next", "hasNext", "total_count", "status"]:
            self.assertIn(key, dict_json, msg=">>>返回数据里面没有该字段：%s" % key)
        self.assertEqual(dict_json["results"][0]["user_id"], "auto_end_user2",
                         msg=">>>断言失败，实际返回结果：%s" % dict_json["results"][0]["user_id"])
        self.assertEqual(dict_json["results"][1]["user_id"], "auto_end_user1",
                         msg=">>>断言失败，实际返回结果：%s" % dict_json["results"][0]["user_id"])
        self.assertEqual(dict_json["total_count"], len(dict_json["results"]),
                         msg=">>>断言失败，实际返回结果：%s" % dict_json["total_count"])

    def test06_get_user_list(self):
        """用户存在：设定返回用户列表数量"""
        self.log.info(message="test05_get_user_list", name="test02_AboutEndUser.py", line=141)
        # 获取测试数据
        method = self.data.get_method(self.sheet, self.row[5])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[5])
        data = self.data.get_param(self.sheet, self.row[5])
        headers = self.hea_data.get_header(self.sheet, self.row[5])
        self.log.info(message="第一步: 获取请求数据")
        self.log.info(message="请求方法：%s" % method)
        self.log.info(message="url：%s" % url)

        # 发送请求
        status_code, res_json = self.http.http_method(method=method, url=url, data=data, headers=headers)
        dict_json = json.loads(res_json)  # 把json数据转换成字典对象
        self.log.info(message="第二步:发送请求，获取返回数据：")
        self.log.info(message="%s" % res_json)

        # 断言
        self.log.info(message="第三步：断言")
        self.assertEqual(status_code, 200, msg=">>>接口请求失败")
        self.assertTrue(dict_json["status"], msg=">>>断言失败，实际返回结果：%s" % dict_json)
        for key in ["results", "previous", "hasPrevious", "next", "hasNext", "total_count", "status"]:
            self.assertIn(key, dict_json, msg=">>>返回数据里面没有该字段：%s" % key)
        self.assertEqual(dict_json["results"][0]["user_id"], "auto_end_user2",
                         msg=">>>断言失败，实际返回结果：%s" % dict_json["results"][0]["user_id"])
        self.assertEqual(dict_json["total_count"], 2, msg=">>>断言失败，实际返回结果：%s" % dict_json["total_count"])
        self.assertEqual(len(dict_json["results"]), 1)

    def test07_get_user_info(self):
        """用户存在：返回用户的详细信息"""
        self.log.info(message="test06_get_user_info", name="test02_AboutEndUser.py", line=167)
        # 获取测试数据
        method = self.data.get_method(self.sheet, self.row[6])
        data = self.data.get_param(self.sheet, self.row[6])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[6]) + data
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
        self.log.info(message="第三步：断言")
        self.assertEqual(status_code, 200, msg=">>>接口请求失败")
        for key in ["user_id", "created_time", "updated_time", "creator", "status"]:
            self.assertIn(key, dict_json, msg=">>>返回数据里面没有该字段：%s" % key)
        self.assertEqual(dict_json["user_id"], "auto_end_user2")
        self.assertEqual(dict_json["creator"], "auto_test")

    def test08_get_user_info(self):
        """用户不存在：无法获取信息"""
        self.log.info(message="test07_get_user_info", name="test02_AboutEndUser.py", line=193)
        # 获取测试数据
        method = self.data.get_method(self.sheet, self.row[7])
        data = self.data.get_param(self.sheet, self.row[7])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[7]) + data
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
        self.log.info(message="第三步：断言")
        self.assertEqual(status_code, 200, msg=">>>接口请求失败")
        self.assertFalse(dict_json["status"], msg=">>>断言失败，实际返回结果：%s" % dict_json)
        self.assertEqual(dict_json["err"]["code"], 404, msg='>>>断言失败，实际返回结果：%s' % dict_json["err"]["code"])
        self.assertEqual(dict_json["err"]["message"], "User doesn't exist",
                         msg='>>>断言失败，实际返回结果：%s' % dict_json["err"]["message"])

    def test09_delete_user(self):
        """删除用户"""
        self.log.info(message="test08_delete_user", name="test02_AboutEndUser.py", line=219)
        # 获取测试数据
        method = self.data.get_method(self.sheet, self.row[8])
        data = self.data.get_param(self.sheet, self.row[8])
        url = self.config.get_base_url() + self.data.get_url(self.sheet, self.row[8]) + data
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

    def test10_delete_user(self):
        """用户不存在：无法获取信息"""
        self.log.info(message="test09_delete_user", name="test02_AboutEndUser.py", line=242)
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
        self.assertFalse(dict_json["status"], msg=">>>断言失败，实际返回结果：%s" % dict_json)
        self.assertEqual(dict_json["err"]["code"], 404, msg='>>>断言失败，实际返回结果：%s' % dict_json["err"]["code"])
        self.assertEqual(dict_json["err"]["message"], "User doesn't exist/already deleted",
                         msg='>>>断言失败，实际返回结果：%s' % dict_json["err"]["message"])


if __name__ == "__main__":
    unittest.main()
