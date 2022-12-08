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
            self.input_text(self.code, code_text, action='输入验证码')
        self.click_element(self.login_btn, action='点击登录')
        # 判断是否有登录前没有登录后页面才有上的一个元素存在，存在说明登录成功，验证码正确，错误则表示验证码或有误，重新识别验证码
        n = 3
        while n := (n - 1) + 1:
            if self.logined():
                print("登录成功")
                break
            # 如果用户名或者密码为空跳出循环，如果不是验证码错误不需要重试
            elif USR == "" or PWD == "":
                break
            else:
                print(f"验证码错误，重新识别,第{4 - n}次")
                code_text = self.get_code_text(self.codepic)
                time.sleep(0.5)
                self.input_text(self.code, code_text, action='输入验证码')
                self.click_element(self.login_btn, action='点击登录')
                n -= 1

        # 加1秒等待，浏览器存储cookie需要时间
        time.sleep(1)

    def logined(self):
        if self.element_is_presence_quick(["css selector", "sup.ivu-badge-count"]):
            return True
        else:
            return False


if __name__ == '__main__':
    [LoginPage().to_loginpage().login(f"", "12345", True) for i in range(2)]
    LoginPage().quit()
