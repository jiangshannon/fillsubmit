# -*- coding: utf-8 -*-
# @__author__:choppa
# @DATA 2022/12/5
# @software:PyCharm
import time

from common.basepage import BasePage
from PageObject.task.menu import Mytask


class Handletask(BasePage):
    def __init__(self):
        super().__init__()
        menu = Mytask()
        menu.go_to_page(menu.pending)
        time.sleep(2)

    def handle_task(self):
        # 点击第一条办理，进入办理界面
        self.move_toclickele(self.handle)
        time.sleep(20)
        # 点击提交按钮


if __name__ == '__main__':
    m = Handletask()
    m.handle_task()
    m.quit()
