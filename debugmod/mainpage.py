# -*- coding: utf-8 -*-
# @__author__:choppa
# @DATA 2021/8/12
import time

from PageObject.login.login_page import LoginPage
from debugmod.basepage import BasePage
from configs.config import host


class MainPage(BasePage):
    #点击选择运输任务公司

    def to_ysgsyw(self):
        self.click_element(self.ysgsyw)

    def to_company(self, action=None):

        # 1-点击第一个公司---
        self.click_element(self.first_co)

    def refresh_bindpage(self):
        self.go_to_page("{}/bindDataManager/bind-data-list".format(host))

    def to_bindDataManager_page(self, action=None):
        self.to_ysgsyw()
        self.to_company()


if __name__ == '__main__':
    LoginPage().to_loginpage().login()
    M = MainPage()
    M.to_bindDataManager_page()
    time.sleep(3)
    M.quit()

