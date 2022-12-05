# -*- coding: utf-8 -*-
# @__author__:choppa
# @DATA 2022/8/4
# @software:PyCharm
# coding:utf-8
import os
import pytest
import time
from selenium import webdriver
from utils.dir_path import chrome_debug_dir
from debugmod.basepage import BasePage
print('执行以debug模式打开浏览器的批处理文件')
# 第一次打开浏览器时启用
# os.popen(chrome_debug_dir)


class DeBg(BasePage):
    def debug_test(self):
        self.get_title_values(self.ysgsyw)


if __name__ == '__main__':
    DeBg().debug_test()

