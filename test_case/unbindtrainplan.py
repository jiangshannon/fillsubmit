# -*- coding: utf-8 -*-
# @__author__:choppa
# @DATA 2022/7/28
# @software:PyCharm

# 进入业务处理界面
from PageObject.bindDataManager.bindDataManager import BindDataManager
from PageObject.login.login_page import LoginPage
from PageObject.login.mainpage import MainPage
#登录
from utils.dir_path import excel_dir
from utils.excelControl_v4 import get_ordercode_data


def unbind(orderdata=None):
    for j in orderdata:
        try:
            # 选择需要解绑绑定的订单并解绑
            BindDataManager().unbind_order(j)
            print("订单号:{} 解绑成功".format(j))
        except Exception as e:
            print("订单号:{} 解绑失败，重试".format(j))
            print(e)
            try:
                # 进入解绑页面
                print("第一次重试")
                MainPage().refresh_bindpage()
                # 选择需要解绑绑定的订单并解绑
                BindDataManager().unbind_order(j)
                print("订单号:{} 解绑成功".format(j))
            except Exception as e:
                print("订单号:{} ，第一次重试失败".format(j))
                print(e)
                try:
                    # 进入解绑页面
                    print("第二次重试")
                    MainPage().refresh_bindpage()
                    # 选择需要解绑绑定的订单并解绑
                    BindDataManager().unbind_order(j)
                    print("订单号:{} 解绑成功，第一次重试成功".format(j))
                except Exception as e:
                    print("订单号:{} ，第二次重试失败，解绑失败".format(j))
                    print(e)


if __name__ == '__main__':
    LoginPage().to_loginpage().login()
    # 选择运输业务的公司
    MainPage().to_bindDataManager_page()
    # 打开绑定管理页面
    MainPage().refresh_bindpage()
    ordercode = get_ordercode_data(excel_dir)
    unbind(ordercode)
    MainPage().quit()
