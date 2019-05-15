# -*- coding: UTF-8 -*-
import requests
import json


class HttpMethod:
    def get_method(self, url, data=None, headers=None):
        try:
            res = requests.get(url=url, params=data, headers=headers)
            status_code = res.status_code
            res_json = res.json()
            return status_code, res_json  # 返回响应码，响应内容
        except Exception as e:
            print("Error:%s" % e)

    def post_method(self, url, data=None, headers=None):
        try:
            res = requests.post(url=url, data=json.dumps(data), headers=headers)
            status_code = res.status_code
            res_json = res.json()
            return status_code, res_json  # 返回响应码，响应内容
        except Exception as e:
            print("Error:%s" % e)

    def put_method(self, url, data=None, headers=None):
        try:
            res = requests.put(url=url, data=json.dumps(data), headers=headers)
            status_code = res.status_code
            res_json = res.json()
            return status_code, res_json  # 返回响应码，响应内容
        except Exception as e:
            print("Error:%s" % e)

    def delete_method(self, url, data=None, headers=None):
        try:
            res = requests.delete(url=url, data=json.dumps(data), headers=headers)
            status_code = res.status_code
            res_json = res.json()
            return status_code, res_json  # 返回响应码，响应内容
        except Exception as e:
            print("Error:%s" % e)

    def http_method(self, method, url, data=None, headers=None):
        if method == 'get':
            status_code, res_json = self.get_method(url, data, headers)
        elif method == 'post':
            status_code, res_json = self.post_method(url, data, headers)
        elif method == 'put':
            status_code, res_json = self.put_method(url, data, headers)
        else:
            status_code, res_json = self.delete_method(url, data, headers)
        return status_code, json.dumps(res_json, ensure_ascii=False, sort_keys=False, indent=2)  # 对json数据进行格式化输出

if __name__ == "__main__":
    h = HttpMethod()
    url = "http://172.16.1.2031:3002/profile/5cd2aaad68d2a00681edaff2"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI1Y2QyYWFiMzY4ZDJhMDA2ODFlZGFmZjMiLCJhdWQiOiJQYW5lbCIsImlzcyI6IlBhbmVsIiwidGVuYW50IjoiaGFpeWl0ZW5hbnQiLCJpYXQiOjE1NTc5MDE4MDAsImV4cCI6MTU4OTQ1OTQwMH0.LUr80U8MBfgz_UYAGq-NiydTBSQwt5AqMP4M_zBuf28"}
    a, b = h.http_method('get', url=url, headers=headers)
    print(a)
    print(b)