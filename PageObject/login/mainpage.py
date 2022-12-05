# -*- coding: utf-8 -*-
# @__author__:choppa
# @DATA 2021/8/12
import time

from PageObject.login.login_page import LoginPage
from common.basepage import BasePage
from configs.config import host


class MainPage(BasePage):
    LoginPage().to_loginpage().login()
    #点击选择运输任务公司
    # dashboard: ['css selector', 'ul.ivu-menu-horizontal a:nth-child(1)']  # 工作台
    # task: ['css selector', 'ul.ivu-menu-horizontal a:nth-child(2)']  # 我的工作
    # service: ['css selector', 'ul.ivu-menu-horizontal a:nth-child(3)']  # 服务中心
    # resource: ['css selector', 'ul.ivu-menu-horizontal a:nth-child(4)']  # 资源管理
    # system: ['css selector', 'ul.ivu-menu-horizontal a:nth-child(5)']  # 系统管理
    # message: ['css selector', 'ul.ivu-menu-horizontal a:nth-child(6)']  # 系统管理






if __name__ == '__main__':
    t = time.time()
    M = MainPage()
    M.click_element(M.task)
    tt = time.time() - t
    print(tt)
    time.sleep(3)
    M.quit()

