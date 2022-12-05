# -*- coding: utf-8 -*-
# @__author__:choppa
# @DATA 2021/8/11
import os
import time

from common.basepage import BasePage
from configs.config import url, usr, pwd


class LoginPage(BasePage):
    def to_loginpage(self):
        self.driver.get(url)
        self.small_window()
        return self

    def login(self, USR=usr, PWD=pwd):
        """
        登录操作,输入的用户，密码，验证码参数化
        :param PWD: 用户
        :param USR: 密码
        :return:
        """
        self.input_text(self.username_input, USR, action='输入用户名')
        self.input_text(self.pwd_input, PWD, action='输入密码')
        self.click_element(self.login_btn, action='点击登录')
        # 加1秒等待，浏览器存储cookie需要时间
        time.sleep(1)


if __name__ == '__main__':
    LoginPage().to_loginpage().login()
    time.sleep(4)
    LoginPage().quit()
