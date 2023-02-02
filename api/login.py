# -*- coding: utf-8 -*-
# @__author__:choppa
# @DATA 2023/2/2
# @software:PyCharm
import random

import ddddocr
import requests

headers = {
    "Accept": "application/json, text/plain, */*",
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


def get_base64_code():
    url = 'http://hn.sjbs.360unicom.cn/api/blade-auth/oauth/captcha'
    data = requests.get(url)
    ret = data.json()
    base64code = ret['image'].strip('data:image/png;base64,')
    uuid1 = ret['key']
    print(uuid1)
    nocr = ddddocr.DdddOcr()
    imagecode = nocr.classification("i" + base64code)
    print("验证码,uuid：", imagecode, uuid1)
    return imagecode, uuid1


def login(usr='admin', pwd='5a6175dd76c9fd0f5c8a1f4089ca6dd0'):
    code = get_base64_code()
    imageCode = code[0]
    uuid1 = code[1]
    url = 'http://hn.sjbs.360unicom.cn/api/blade-auth/oauth/tokenWithBody'
    data = {"username": usr, "password": pwd,
            "tenantId": "000000", "userType": "web", "grant_type": "password",
            "uuid": uuid1, "imageCode": imageCode}
    head = {
            "Authorization": "Basic c2FiZXI6c2FiZXJfc2VjcmV0",
            }
    res = requests.post(url, json=data, headers=head)
    print(res.json()['data']['accessToken'])
    return res.json()


def addusr(name, dpid):
    url = "http://hn.sjbs.360unicom.cn/api/blade-user/submit"
    data = {"realName": "s" + name, "account": "s" + name,
            "deptId": dpid, "phone": "159" + str(random.randint(1111111, 9999999)),
            "roleId": "1619886122085670913", "sex": 1, "password": "Sjbs@2022", "remark": "", "status": 1}
    res = requests.post(url, json=data, headers=headers)
    print(res.json())
    return res.json()


login()
