# -*- coding: utf-8 -*-
# @__author__:choppa
# @DATA 2022/12/5
# @software:PyCharm
import time

from PageObject.login.mainpage import MainPage
from common.basepage import BasePage


class Mytask(BasePage):
    pending = "http://hn.sjbs.360unicom.cn/work/task/pending"  # 我的代办
    finished = "http://hn.sjbs.360unicom.cn/work/task/finished"  # 我的已办
    distribute = "http://hn.sjbs.360unicom.cn/work/task/distribute"  # 我的分发
    approval = "http://hn.sjbs.360unicom.cn/work/task/approval"  # 待我审批
    has_approval = "http://hn.sjbs.360unicom.cn/work/task/has-approved"  # 我的已审

    def go_page(self):
        self.go_to_page(self.pending)
        time.sleep(1)
        self.go_to_page(self.finished)
        time.sleep(1)
        self.go_to_page(self.distribute)
        time.sleep(1)
        self.go_to_page(self.approval)
        time.sleep(1)
        self.go_to_page(self.has_approval)


if __name__ == '__main__':
    M = MainPage()
    t = time.time()
    M.click_element(M.task)
    N= Mytask()
    M.go_page()
    M.quit()
