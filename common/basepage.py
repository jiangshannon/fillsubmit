# -*- coding: utf-8 -*-
# @__author__:choppa
# @DATA 2021/8/10
import time

import ddddocr
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

    def wait_elevisible(self, bloc, timeout=5, frequency=0.5):
        bele = WebDriverWait(self.driver, timeout, frequency).until(EC.visibility_of_element_located(bloc))
        return bele

    def wait_presence(self, bloc, timeout=1.5, frequency=0.5):
        bele = WebDriverWait(self.driver, timeout, frequency).until(EC.presence_of_element_located(bloc))
        return bele

    def wait_clickable(self, bloc, timeout=1.5, frequency=0.5):
        bele = WebDriverWait(self.driver, timeout, frequency).until(EC.element_to_be_clickable(bloc))
        return bele

    def get_element(self, bloc):
        bele = self.driver.find_element(bloc)
        return bele

    def input_text(self, bloc, *args, action=''):
        bele = self.wait_presence(bloc)
        bele.clear()
        bele.send_keys(*args)

    def get_current_url(self):
        url = self.driver.current_url
        print(url)
        return url

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
            WebDriverWait(self.driver, timeout, frequency).until(EC.presence_of_element_located(bloc))
        except Exception as e:
            return False
        return True

    def element_is_presence_quick(self, bloc):
        """
        创建一个判读元素是否存在的方法，捕获显示等待下元素是否返回traceback信息
        return True表明元素存在
        return Flase表示元素不存在
        :param bloc: 元素
        :return: 存在返回True，不存在返回Flase
        """
        try:
            self.driver.find_element(*bloc)
        except Exception as e:
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

    def move_toeleposition(self):
        t1 = time.time()
        AC = webdriver.ActionChains(self.driver)
        AC.move_by_offset(747, 473).click().perform()
        AC.reset_actions()

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

    def get_title_values(self, bloc):
        ele = self.get_ele_location(bloc)
        return ele.get_attribute('title')

    def get_code_text(self, bloc):
        ocr = ddddocr.DdddOcr()
        pic = self.driver.find_element(*bloc).screenshot_as_png
        res = ocr.classification(pic)
        print("验证码是：", res)
        return res


if __name__ == '__main__':
    nocr = ddddocr.DdddOcr()
    res = nocr.classification('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')
    print("验证码是：", res)

