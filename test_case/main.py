# -*- coding: utf-8 -*-
# @__author__:choppa
# @DATA 2022/8/4
# @software:PyCharm
import threading
import time

from PageObject.login.login_page import LoginPage
from PageObject.login.mainpage import MainPage
from test_case.bindtrainplan import bindorder
from test_case.unbindtrainplan import unbind
from utils.dir_path import excel_dir
from utils.excelControl_v4 import get_ordercode_data, get_taskcode_data

# 火运计划数据
taskdata = get_taskcode_data(excel_dir)
# 订单数据
orderdata = get_ordercode_data(excel_dir)
# 登录

LoginPage().to_loginpage().login()
# 选择运输业务的公司
MainPage().to_bindDataManager_page()
# 打开绑定管理页面
MainPage().refresh_bindpage()
s = time.time()


# 解绑
def unbind_t():
    unbind(orderdata)


# 绑定
def bind_t():
    bindorder(taskdata, orderdata)


# threads = []
# for i in range(9):
#     t = threading.Thread(target=bind_t)
#     threads.append(t)
#     time.sleep(0.1)
#     threads[i].start()
# print("耗时:{:.2f}".format(time.time() - s))
# MainPage().quit()
bind_t()
# unbind_t()