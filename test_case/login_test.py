# -*- coding: utf-8 -*-
# @__author__:choppa
# @DATA 2022/12/8
# @software:PyCharm
import pytest

from PageObject.login.login_page import LoginPage
from utils.dir_path import excel_dir
from utils.excelControl_v4 import get_login_data


class Testlogin:

    @pytest.mark.parametrize("usr,pwd,EC", get_login_data(excel_dir, "login"))
    def test_login(self, usr, pwd, EC):
        LoginPage().to_loginpage().login(usr, pwd)
        # 判断是否登录成功
        assert LoginPage().logined() == int(EC)


if __name__ == '__main__':
    pytest.main()
