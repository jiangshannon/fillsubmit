# -*- coding: utf-8 -*-
# @__author__:choppa
# @DATA 2022/7/28
# @software:PyCharm
import time

import pyautogui
import pyperclip

from PageObject.login.login_page import LoginPage
from PageObject.login.mainpage import MainPage
from common.basepage import BasePage

# 控制输入速度 单位秒
T = 1


class BindDataManager(BasePage):
    def choose_bindplan(self, bp_cartask='QR20220619002', bp_divtask='FJ2041275', bp_trainplan='7月1号第二个火运计划'):
        """

        :param bp_cartask: 汽运任务
        :param bp_divtask:  分解任务
        :param bp_trainplan:  火运计划
        :return:
        """
        # 点击绑定火运计划任务
        self.click_element(self.blindplan)
        # 输入汽运任务
        self.click_element(self.bp_cartask)
        pyautogui.typewrite(bp_cartask)
        time.sleep(T)
        pyautogui.hotkey('enter')
        # 输入分解任务
        self.click_element(self.bp_divtask)
        pyautogui.typewrite(bp_divtask)
        time.sleep(T)
        pyautogui.hotkey('enter')
        self.click_element(self.bp_trainplan)
        # 输入火运计划
        pyperclip.copy(bp_trainplan)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(T)
        pyautogui.hotkey('enter')
        # 判断火运计划输入结果是否和输入一致
        assert bp_cartask in self.get_title_values(self.s_cartask)
        assert bp_divtask in self.get_text_value(self.s_divtask)
        assert bp_trainplan in self.get_title_values(self.s_trainplan)
        # 确认绑定任务
        self.click_element(self.submit_but)

    def bind_order(self, ordernum=None):
        # 输入获取到的订单号到派单号搜索框里
        self.input_text(self.input_carorder, ordernum)
        # 点击搜索按钮
        self.click_element(self.searchbut)
        # 勾选第一个订单
        self.move_toclickele(self.checkbox)
        # 点击确认
        self.js_click(self.buttom_confirmbot)

    def check_result(self):
        pass

    def unbind_order(self, odernum=None):
        # 输入运单号
        self.input_text(self.unborders, odernum)
        # 搜素运单号
        self.click_element(self.unbsearchbut)
        # 点击解绑
        self.click_element(self.unbconfirm)
        # 弹窗二次确认
        self.click_element(self.unbsec_confirm)


if __name__ == '__main__':
    start = time.time()
    try:
        BindDataManager().unbind_order("P12206216610")
    except Exception as e1:
        print(e1)
    T = time.time() - start
    print(T)
