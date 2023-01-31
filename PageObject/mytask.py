# -*- coding: utf-8 -*-
# @__author__:choppa
# @DATA 2023/1/31
# @software:PyCharm
import time

from PageObject.login.mainpage import LoginPage
from PageObject.login.mainpage import MainPage
from common.basepage import BasePage


class Mytask(BasePage):

    def handle_mytask(self,t=6):
        self.go_to_page(self.pending)
        self.move_toclickele(self.handle)
        time.sleep(t)
        self.move_toclickele(self.submit)
        self.move_toclickele(self.confirm)
        # 等待请求处理完成
        time.sleep(0.8)


if __name__ == '__main__':
    LoginPage().to_loginpage().login(USR="p0", PWD="123456")
    MainPage().menus("task")
    Mytask().handle_mytask()




