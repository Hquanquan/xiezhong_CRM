# -*- encoding: utf-8 -*-
"""
@File    :   login_page.py
@Time    :   2020/07/06 21:15:46
@Author  :   黄权权
@Desc    :   登录页面-元素和方法
"""

# here put the import lib

# 为了导入自定义的包
import os
import sys

# __file__获取执行文件相对路径，整行为取上一级的上一级目录
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(BASE_DIR)

import random
from units.base_page import BasePage


class LoginPage(BasePage):  # 继承basePage类

    # 用户输入框
    username = 'id=>username'

    # 输入用户名
    def send_username(self, userName):
        self.send_keys(self.username, userName)

    # 密码输入框
    password = 'id=>password'

    # 输入密码
    def send_password(self, passWord):
        self.send_keys(self.password, passWord)

    # 登录按钮
    loginBtn = 'xpath=>//*[@id="login"]/form/div[2]/div[2]/button'

    # 点击登录按钮
    def click_loginBtn(self):
        self.click(self.loginBtn)

    # 错误提示框
    errorText = 'class_name=>layui-layer-padding'

    # 获取错误的提示语
    def get_alterText(self):
        return self.get_text(self.errorText)

    # 成功提示语
    successText = 'class_name=>layui-layer-msg'

    # 获取登录成功的提示语
    def get_successText(self):
        return self.get_text(self.successText)
