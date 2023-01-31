# -*- coding: utf-8 -*-
# @__author__:choppa
# @DATA 2023/1/31
# @software:PyCharm
from PageObject.login.login_page import LoginPage
from PageObject.login.mainpage import MainPage
from PageObject.mytask import Mytask

for i in range(50, 70):
    try:
        print("当前用户{}".format(i))
        LoginPage().to_loginpage().login(USR=f"p{i}", PWD="123456")
        MainPage().menus("task")
        Mytask().handle_mytask()
        # a = input("是否继续，Y继续")
        # if str(a) == "y" or "Y":
        #     print("用户{}已完成".format(i))
    except Exception as e:
        print(e)
        try:
            print("超时，加8秒等待时间")
            LoginPage().to_loginpage().login(USR=f"p{i}", PWD="123456")
            MainPage().menus("task")
            Mytask().handle_mytask(8)
        except Exception as e:
            print(e)
            print("超时，加12秒等待时间")
            LoginPage().to_loginpage().login(USR=f"p{i}", PWD="123456")
            MainPage().menus("task")
            Mytask().handle_mytask(12)


print("全部完成,关闭浏览器")
