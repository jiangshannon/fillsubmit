# -*- coding: utf-8 -*-
# @__author__:choppa
# @DATA 2022/12/21
# @software:PyCharm
from common.basepage import BasePage
from PageObject.login.mainpage import MainPage

class Service(BasePage):

    def __init__(self):
        super().__init__()
        MainPage().menus("service")

    def create_task(self):
        self.click_element()