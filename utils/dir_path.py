# -*- coding: utf-8 -*-
# @__author__:choppa
# @DATA 2021/8/19
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#out
logs_dir = os.path.join(base_dir, r'outFiles\logs')
report_dir = os.path.join(base_dir, r'outFiles\report')
screenshot_dir = os.path.join(base_dir, r'outFiles\screenshot')

#in
config_dir = os.path.join(base_dir, r'configs\config.py')
yaml_dir = os.path.join(base_dir, r'configs\locators.yaml')
data_dir = os.path.join(base_dir, r'common\data')
docs_dir = os.path.join(base_dir, r'common\docs')
excel_dir = os.path.join(base_dir,r'common\data\data.xlsx')


PageLocators_dir = os.path.join(base_dir, r'odls')
PageObjct_dir = os.path.join(base_dir, r'ageObjct_dir')
test_case_dir = os.path.join(base_dir, r'test_case')
utils_dir = os.path.join(base_dir, r'utils')
chrome_debug_dir = os.path.join(base_dir,r'common\data\chrome.bat')

if __name__ == '__main__':
    print(base_dir)
    print(docs_dir)
    print(logs_dir)
    print(screenshot_dir)
    print(utils_dir)
    print(yaml_dir)
    print(chrome_debug_dir)
