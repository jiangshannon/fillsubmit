# -*- coding: utf-8 -*-
# @__author__:choppa
# @DATA 2022/7/28
# @software:PyCharm

# 进入业务处理界面
from PageObject.bindDataManager.bindDataManager import BindDataManager
from PageObject.login.login_page import LoginPage
from PageObject.login.mainpage import MainPage

# 登录
from utils.dir_path import excel_dir
from utils.excelControl_v4 import get_taskcode_data, get_ordercode_data
# 获取数据

global j


def bindorder(taskdata=None, orderdata=None):
    """

    :param taskdata: 绑定火运计划三个参数，,类型list
    :param orderdata: 订单号
    :return:
    """
    global j
    if taskdata and isinstance(taskdata, list):
        for i in taskdata:
            if orderdata and isinstance(orderdata, list):
                for j in orderdata:
                    n = 1
                    while n <= 2:
                        try:
                            # 选择汽运任务，分解任务，火运计划
                            BindDataManager().choose_bindplan(i[0], i[1], i[2])
                            # 选择需要绑定的订单并绑定
                            BindDataManager().bind_order(j)
                            print("任务号:{}，分解任务:{}，火运计划:{}，订单号:{} 绑定成功".format(i[0], i[1], i[2], j))
                            break
                        except Exception as e:
                            print("===任务号:{}，分解任务:{}，火运计划:{}，订单号:{} 绑定失败，重试 ===".format(i[0], i[1], i[2], j))
                            print(e)
                            MainPage().refresh_bindpage()
                            print("第{}次重试失败".format(n))
                            n += 1
            else:
                print("orderdata必须为非空列表")
    else:
        print("datalist必须为非空列表")


if __name__ == '__main__':
    LoginPage().to_loginpage().login()
    # 选择运输业务的公司
    MainPage().to_bindDataManager_page()
    # 打开绑定管理页面
    MainPage().refresh_bindpage()
    taskdata1 = get_taskcode_data(excel_dir)
    orderdata1 = get_ordercode_data(excel_dir)
    bindorder(taskdata1, orderdata1)
    MainPage().quit()