# -*- coding: utf-8 -*-
# @__author__:choppa
# @DATA 2021/8/12
import time

from PageObject.login.login_page import LoginPage
from common.basepage import BasePage


class MainPage(BasePage):
    """
    # dashboard: ['css selector', 'ul.ivu-menu-horizontal a:nth-child(1)']  # 工作台
    # task: ['css selector', 'ul.ivu-menu-horizontal a:nth-child(2)']  # 我的工作
    # service: ['css selector', 'ul.ivu-menu-horizontal a:nth-child(3)']  # 服务中心
    # resource: ['css selector', 'ul.ivu-menu-horizontal a:nth-child(4)']  # 资源管理
    # system: ['css selector', 'ul.ivu-menu-horizontal a:nth-child(5)']  # 系统管理
    # message: ['css selector', 'ul.ivu-menu-horizontal a:nth-child(6)']  # 系统管理
    可选参数  dashboard，task，service，resource，system，message
    """

    def menus(self, menu):
        """

        :param menu: 菜单名 dashboard，task，service，resource，system，message
        :return:
        """
        if menu == "dashboard":
            self.click_element(self.dashboard)
        elif menu == "task":
            self.click_element(self.task)
        elif menu == "service":
            self.click_element(self.service)
        elif menu == "resource":
            self.click_element(self.resource)
        elif menu == "system":
            self.click_element(self.system)
        elif menu == "message":
            self.click_element(self.message)
        else:
            print("菜单不存在，【dashboard，task，service，resource，system，message】可用")

if __name__ == '__main__':
    t = time.time()
    LoginPage().to_loginpage().login()
    m = MainPage()
    m.menus("task")
    tt = time.time() -t
    print(tt)
