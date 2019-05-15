import requests
import json

#data = {"limit": 1}
data = "5cd2aaad68d2a00681edaff2"
try:
    url = "http://172.16.1.201:3002/profile"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI1Y2QyYWFiMzY4ZDJhMDA2ODFlZGFmZjMiLCJhdWQiOiJQYW5lbCIsImlzcyI6IlBhbmVsIiwidGVuYW50IjoiaGFpeWl0ZW5hbnQiLCJpYXQiOjE1NTc5MDUwOTcsImV4cCI6MTU4OTQ2MjY5N30.3-DeoZuqIkU5x90WPALEqSpcGVU2gXVDUw4itouHo4c"}
    res = requests.get(url=url, params=data, headers=headers)
    status_code = res.status_code
    print(status_code)
    print(res.json())
# except BaseException as e:
except Exception as e:
    print("Error:%s" % e)