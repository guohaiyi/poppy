# -*- coding: UTF-8 -*-
import requests
import json


class HttpMethod:
    def get_method(self, url, data=None, headers=None):
        if isinstance(data, dict):
            try:
                res = requests.get(url=url, params=data, headers=headers).json()
                return res
            except Exception as e:
                print("Error:%s" % e)
        else:
            try:
                res = requests.get(url=url + "/" + data, headers=headers).json()
                return res
            except Exception as e:
                print("Error:%s" % e)

    def post_method(self, url, data=None, headers=None):
        try:
            res = requests.post(url=url, data=json.dumps(data), headers=headers).json()
            return res
        except Exception as e:
            print("Error:%s" % e)

    def put_method(self, url, data=None, headers=None):
        if isinstance(data, dict):
            try:
                res = requests.put(url=url, data=json.dumps(data), headers=headers).json()
                return res
            except Exception as e:
                print("Error:%s" % e)
        else:
            try:
                res = requests.put(url=url + "/" + data, headers=headers).json()
                return res
            except Exception as e:
                print("Error:%s" % e)

    def delete_method(self, url, data=None, headers=None):
        if isinstance(data, dict):
            try:
                res = requests.delete(url=url, data=json.dumps(data), headers=headers).json()
                return res
            except Exception as e:
                print("Error:%s" % e)
        else:
            try:
                res = requests.delete(url=url + "/" + data, headers=headers).json()
                return res
            except Exception as e:
                print("Error:%s" % e)

    def http_method(self, method, url, data, headers):
        if method == 'get':
            res = self.get_method(url, data, headers)
        elif method == 'post':
            res = self.post_method(url, data, headers)
        elif method == 'put':
            res = self.put_method(url, data, headers)
        else:
            res = self.delete_method(url, data, headers)
        return json.dumps(res, ensure_ascii=False, sort_keys=False, indent=2)   # 对json数据进行格式化输出


if __name__ == "__main__":
    h = HttpMethod()
    url = "http://172.16.1.97:3002/profile"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI1YmZmNWQxNjE4ZjJmNjUxNGE0OGUzODQiLCJhdWQiOiJQYW5lbCIsImlzcyI6IlBhbmVsIiwidGVuYW50IjoiaGFpeWl0ZW5hbnQiLCJpYXQiOjE1NDM1NjY2NTYsImV4cCI6MTU3NTEyNDI1Nn0.JSoi66llSbuFQPjeliOWsW4oImTSjnjPGKSovBv3P6A"}
    # data = "5bfe667618f2f6514a48ccde"
    data = {"limit": 1}
    s = h.http_method('get', url, data, headers)
    print(s)
