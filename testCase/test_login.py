# -*- encoding: utf-8 -*-
"""
@Author: 黄权权
@Date: 2020-07-06 22:03:56
@LastEditors: 黄权权
@LastEditTime: 2020-07-10 11:05:05
@Descripttion:登录测试类
"""
# here put the import lib
import unittest
import time
import threading
# 为了导入自定义的包
import sys, os
# __file__获取执行文件相对路径，整行为取上一级的上一级目录
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(BASE_DIR)
from framework.browser import Browser
from pageobjects.login_page import LoginPage


class Login(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        初始化操作
        打开浏览器
            1、实例化一个浏览器对象 browser
                1、先创建一个浏览器的类 Browser,已在frameword文件夹创建该类
                2、导入该类，使用from framework.browser import Browser导入，注意
                3、实例化对象 browser = Browser(cls)
            2、调用browser打开浏览器,并赋值给cls.driver使其成为该测试类的属性:
             cls.driver = browser.open_browser(cls)
        """
        cls.browser = Browser(cls)
        cls.driver = cls.browser.open_browser(cls)
        cls.loginPage = LoginPage(cls.driver)
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        # cls.driver.quit()
        print('tearDownClass')
        pass

    def test_0001(self):
        """验证是登录页面"""
        title = self.loginPage.get_url_title()
        self.assertEqual(title, 'CRM管理系统 - 登录')
        time.sleep(0.5)

    def test_0002(self):
        """空用户名，空密码，验证无法登录"""
        self.loginPage.send_username('')
        self.loginPage.send_password('')
        time.sleep(0.5)
        self.loginPage.click_loginBtn()
        text = self.loginPage.get_alterText()
        print(text)
        self.assertEqual("必填项不能为空", text)
        time.sleep(0.5)

    def test_0003(self):
        """正确的用户名，错误的密码，验证登录失败"""
        self.loginPage.send_username("17288449102")
        self.loginPage.send_password("15626268694")
        time.sleep(0.5)
        self.loginPage.click_loginBtn()
        time.sleep(1)
        # 获取错误提示语
        text = self.loginPage.get_alterText()
        print(text)
        self.assertEqual(text, '密码错误')
        time.sleep(1)

    def test_0004(self):
        """未注册的用户名和密码，验证登录失败"""
        self.loginPage.send_username("15626268694")
        self.loginPage.send_password("17288449102")
        time.sleep(0.5)
        self.loginPage.click_loginBtn()
        time.sleep(1)
        # 获取错误提示语
        text = self.loginPage.get_alterText()
        print(text)
        # self.assertEqual(text,'密码1错误',"出错的用例是："+sys._getframe().f_code.co_name)
        self.assertEqual(text, '手机号不存在')
        time.sleep(1)

    def test_0005(self):
        """正确用户名，空密码，验证登录失败"""
        self.loginPage.send_username('17288449102')
        time.sleep(0.5)
        self.loginPage.send_password('')
        time.sleep(0.5)
        self.loginPage.click_loginBtn()
        text = self.loginPage.get_alterText()
        print(text)
        self.assertEqual("必填项不能为空", text)
        time.sleep(1)

    # @unittest.skip("暂不执行")
    def test_0006(self):
        """正确用户名，正确密码，验证登录成功"""
        self.loginPage.send_username('15521200433')
        self.loginPage.send_password('15521200433')
        time.sleep(0.5)
        self.loginPage.click_loginBtn()
        time.sleep(0.5)
        # 点击登录按钮后登录成功，进入首页，获取首页title，进行验证是否登录成功
        home_title = self.loginPage.get_url_title()
        self.assertEqual(home_title, 'CRM管理系统')
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
    unittest.main(verbosity=2)
