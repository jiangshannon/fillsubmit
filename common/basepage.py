# -*- coding: utf-8 -*-
# @__author__:choppa
# @DATA 2021/8/10
import time

import pyautogui
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from common.mydriver import Mydriver
from utils.yaml_reader import read_yaml_data, dir_path


class BasePage(object):
    def __init__(self):
        self.driver = Mydriver().get_mydriver()
        loadlocators = read_yaml_data(dir_path.yaml_dir)[self.__class__.__name__]
        for k, v in loadlocators.items():
            setattr(self, k, v)

    def wait_elevisible(self, bloc, timeout=10, frequency=0.5):
        bele = WebDriverWait(self.driver, timeout, frequency).until(EC.visibility_of_element_located(bloc))
        return bele

    def wait_presence(self, bloc, timeout=1.5, frequency=0.5):
        bele = WebDriverWait(self.driver, timeout, frequency).until(EC.presence_of_element_located(bloc))
        return bele

    def wait_clickable(self, bloc, timeout=10, frequency=0.5):
        bele = WebDriverWait(self.driver, timeout, frequency).until(EC.element_to_be_clickable(bloc))
        return bele

    def get_element(self, bloc):
        bele = self.driver.find_element(bloc)
        return bele

    def input_text(self, bloc, *args, action=''):
        bele = self.wait_presence(bloc)
        bele.clear()
        bele.send_keys(*args)

    def input_text_1(self, bloc, *args, action=''):
        bele = self.wait_presence(bloc)
        bele.send_keys(*args)

    def clear_data(self, bloc, action=''):
        bele = self.wait_elevisible(bloc)
        bele.clear()

    def click_element(self, bloc, action=''):
        bele = self.wait_clickable(bloc)
        bele.click()

    def click_element_clickable(self, bloc, action=''):
        bele = self.wait_clickable(bloc)
        bele.click()

    def element_is_presence(self, bloc, timeout=1.5, frequency=0.5):
        """
        创建一个判读元素是否存在的方法，捕获显示等待下元素是否返回traceback信息
        return True表明元素存在
        return Flase表示元素不存在
        :param frequency: 频次
        :param timeout: 持续时间
        :param bloc: 元素
        :return: 存在返回True，不存在返回Flase
        """
        try:
            WebDriverWait(self.driver, timeout, frequency).until(EC.element_to_be_clickable(bloc))
            print(f'元素存在')
        except Exception as e:
            print(e)
            print(f'未找到元素')
            return False
        return True

    def get_screenshot(self):
        curtime = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
        self.driver.save_screenshot(curtime, dir_path.screenshot_dir)

    def go_to_page(self, pageurl):
        self.driver.get(pageurl)

    def quit(self):
        self.driver.quit()

    def get_text_value(self, bloc):
        bele = self.driver.find_element(*bloc)
        return bele.get_attribute("textContent")

    def get_ele_location(self, bloc):
        bele = self.driver.find_element(*bloc)
        return bele

    def move_toclickele(self, bloc):
        ele = self.wait_presence(bloc)
        webdriver.ActionChains(self.driver).move_to_element(ele).click().perform()

    def is_selected(self, bloc=None):
        ele = self.driver.find_element(bloc)
        if ele.is_selected():
            print('元素已选中')
        else:
            print("元素未选中")

    def small_window(self):
        pyautogui.hotkey('ctrl', '-')

    def js_click(self, bloc):
        ele = self.wait_presence(bloc)
        self.driver.execute_script("arguments[0].click();", ele)

    def test(self, bloc):
        ele = self.driver.find_elements(*bloc)
        print(len(ele))

    def get_title_values(self,bloc):
        ele = self.get_ele_location(bloc)
        return ele.get_attribute('title')


if __name__ == '__main__':
    pass
