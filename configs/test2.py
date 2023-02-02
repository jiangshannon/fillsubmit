# -*- coding: utf-8 -*-
# @__author__:choppa
# @DATA 2023/1/31
# @software:PyCharm
import random
import time

import grequests

start_time = time.time()
# Create a 10000 requests
headers = {
    "Blade-Auth": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJpc3N1c2VyIiwiYXVkIjoiYXVkaWVuY2UiLCJ"
                  "yZWFsTmFtZSI6IueuoeeQhuWRmCIsInJvbGVJZCI6IjExMjM1OTg4MTY3Mzg2NzUyMDEiLCJ0ZW5hbnRJZCI6I"
                  "jAwMDAwMCIsImRlcHRJZCI6IjExMjM1OTg4MTM3Mzg2NzUyMDEiLCJyb2xlTmFtZSI6ImFkbWluaXN0cmF0b3IiL"
                  "CJwb3N0SWQiOiIxMTIzNTk4ODE3NzM4Njc1MjAxIiwidG9rZW5UeXBlIjoiYWNjZXNzVG9rZW4iLCJ1c2VySWQiOi"
                  "IxMTIzNTk4ODIxNzM4Njc1MjAxIiwiYWNjb3VudCI6ImFkbWluIiwiY2xpZW50X2lkIjoic2FiZXIiLCJleHAiOjE2"
                  "Nzc4MzkwNjcsIm5iZiI6MTY3NTI0NzA2N30.KUS7m_8QzZAGkLDh-yZ1Mman-pnciQZCAmbckJYTcXw",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 "
                  "Safari/537.36",
    "Content-Type": "application/json;charset=UTF-8",
}

deptlist = ['1613800042701459458', '1613800659113152513', '1600675457755934726', '1600675457755934729',
            '1597841966232129538', '1597841961857470465', '1597841959013732354']

urls = ["http://hn.sjbs.360unicom.cn/api/blade-user/submit"] * 1
data = {"realName": "you" + str(random.randint(11111, 999999)), "account": "you" + str(random.randint(11111, 999999)),
         "deptId": random.choice(deptlist), "phone": "159" + str(random.randint(11111111, 99999999)),
         "roleId": "1619886122085670913", "sex": 1, "password": "Sjbs@2022", "remark": "", "status": 1}
rs = (grequests.post(u, json=data, headers=headers) for u in urls)

# Send them.
grequests.map(rs)

print(time.time() - start_time)  # Result was: 9.66666889191
