# -*- coding: utf-8 -*-
# @__author__:choppa
# @DATA 2021/8/11
import time

from common.basepage import BasePage
from configs.config import url, usr, pwd


class LoginPage(BasePage):
    def to_loginpage(self):
        self.driver.get(url)
        return self

    def login(self, USR=usr, PWD=pwd, hascode=True):
        """
        登录操作,输入的用户，密码，验证码参数化
        :param hascode: 是否有验证码
        :param PWD: 用户
        :param USR: 密码
        :return:
        """
        self.input_text(self.username_input, USR, action='输入用户名')
        self.input_text(self.pwd_input, PWD, action='输入密码')
        if hascode:
            code_text = self.get_code_text(self.codepic)
            time.sleep(1)
            self.input_text(self.code,code_text, action='输入验证码')
        self.click_element(self.login_btn, action='点击登录')
        # 加1秒等待，浏览器存储cookie需要时间
        time.sleep(1)
        if not self.element_is_presence_quick(["css selector", "div.ivu-form-item-error-tip"]):
            pass
        else:
            self.input_text(self.username_input, USR, action='输入用户名')
            self.input_text(self.pwd_input, PWD, action='输入密码')
            if hascode:
                code_text = self.get_code_text(self.codepic)
                time.sleep(1)
                self.input_text(self.code, code_text, action='输入验证码')
            self.click_element(self.login_btn, action='点击登录')
            print("验证码错误，重新识别")


if __name__ == '__main__':
    for i in range(1):
        LoginPage().to_loginpage().login(usr, pwd, True)
        # time.sleep(1)
    LoginPage().quit()
