# -*- coding: utf-8 -*-
# @__author__:choppa
# @DATA 2023/1/31
# @software:PyCharm
from PageObject.login.login_page import LoginPage
from PageObject.login.mainpage import MainPage
from PageObject.mytask import Mytask

for i in range(44, 101):
        n = 3
        while n := (n - 1) + 1:
            try:
                usrname="q"+str(i).zfill(3)
                print("当前用户{}".format(usrname))
                LoginPage().to_loginpage().login(USR=usrname, PWD="Sjbs@2022")
                MainPage().menus("task")
                Mytask().handle_mytask((4-n)*5)
                print((4-n)*5)
                # a = input("是否继续，Y继续")
                # if str(a) == "y" or "Y":
                # print("用户{}已完成".format(i))
                n = 0
            except Exception as e:
                print(e)
                n -= 1
Mytask().quit()
print("全部完成,关闭浏览器")
