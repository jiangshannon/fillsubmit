# -*- coding: utf-8 -*-
# @__author__:choppa
# @DATA 2021/8/17
import os

import pyautogui
from selenium import webdriver
import time

from selenium.webdriver.chrome.options import Options


class Single(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance


class Mydriver(Single):
    driver = None

    def get_mydriver(self, browser_name='chrome'):
        if self.driver is None:
            if browser_name == 'chrome':
                # debug 请求设置 26-29行
                # chrome_options = Options()
                # chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
                # self.driver = webdriver.Chrome(options=chrome_options)
                # 正常请求driver
                self.driver = webdriver.Chrome()
            elif browser_name == 'firefox':
                self.driver = webdriver.Firefox()
            elif browser_name == 'edge':
                self.driver = webdriver.Edge()
            else:
                print(f"找不到{browser_name}浏览器")
            self.driver.implicitly_wait(5)
            self.driver.maximize_window()
        return self.driver


if __name__ == '__main__':
    Mydriver().get_mydriver().get("http://123.56.174.87:8084/user/login")
    Mydriver().get_mydriver().execute_script("document.body.style.zoom='0.8'")
    time.sleep(4)
    Mydriver().get_mydriver().quit()
