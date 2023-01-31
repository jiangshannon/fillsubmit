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

    def forgetpassword(self):
        self.go_to_page("http://hn.sjbs.360unicom.cn/forget")

    def reset_password(self, newpw, renewpd, phoneno):
        self.input_text(self.newpw, newpw)
        self.input_text(self.rpnewpw, renewpd)
        self.input_text(self.phoneno, phoneno)
        self.click_element(self.getcode)

    def brute_force(self, code):
        self.input_text(self.retcode, code)
        self.move_toeleposition()

    def atloginpage(self):
        if self.element_is_presence_quick(self.codepic):
            return True
        else:
            return False

    def logined(self):
        if self.element_is_presence_quick(["css selector", "ul.ivu-menu-horizontal a:nth-child(1)"]):
            return True
        else:
            return False


if __name__ == '__main__':
    lista = ["p0", "p1", "p2", "p3", "p4", "p850", "p860", "p900"]

    listb = ["iosapp1000", "iosapp500", "iosapp0", "iosapp800"]
    listc = ["iosapp901"]
    for i in range(50):
        print("当前用户{}".format(i))
        LoginPage().to_loginpage().login(USR=f"p{i}", PWD="123456")
        a = input("是否继续，Y继续")
        if str(a) == "y" or "Y":
            print("用户{}已完成".format(i))
    print("全部完成,关闭浏览器")
    time.sleep(10)
    LoginPage().quit()
