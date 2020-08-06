"""
@Author: 黄权权
@Date: 2020-07-03 11:56:02
@LastEditors: 黄权权
@LastEditTime: 2020-07-10 17:05:42
@Descripttion:
"""
# -*- encoding: utf-8 -*-
# here put the import lib

# (为了防止乱码问题,以及在程序中添加中文注释,把编码统一成UTF-8;)
# coding = utf-8

# (导入selenium的webdriver包,导入webdriver包后才能使用webdriver API进行自动化脚本开发.)
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# (将控制的webdriver的Chrome赋值给browser,获得了浏览器对象才可以启动浏览器;)
browser = webdriver.Chrome(r'E:\python\chromedriver_win32\chromedriver.exe')
# browser = webdriver.Firefox()

# 设置超时时间10秒
browser.implicitly_wait(10)
#设置窗口最大化
browser.maximize_window()

# (获得浏览器对象后,通过get()方法,向浏览器发送网址;)
browser.get('http://192.168.1.173/crmViewX/login.html')
# 通过id找到用户输入框和密码输入框
username = browser.find_element_by_id('username')
password = browser.find_element_by_id('password')

# 防止输入框中有内容，先请空输入框
username.clear()
password.clear()

# 输入用户名和密码
username.send_keys('17288449102')
password.send_keys('17288449102')

# 找到登录按钮并点击
loginBtn = browser.find_element_by_xpath('//*[@id="login"]/form/div[2]/div[2]/button')
loginBtn.click()
# 提示框
# 成功提示框 layui-layer layui-layer-dialog layui-layer-border layui-layer-msg
# 失败提示框 layui-layer-content layui-layer-padding
print("==============================================")
""" 
try:
    # successtext = browser.find_element_by_class_name('layui-layer-msg')
    # print(successtext)
    # print(successtext.text) 
    # errortext = browser.find_element_by_class_name('layui-layer-padding')
    # print(errortext)
    # print(errortext.text)
    pass
except Exception as e:
    print(e)
    pass

 """


""" 
# 消息icon
time.sleep(2)
text = browser.find_element_by_css_selector('#notice > span')
print("===========>:")
print("+++++%s"%text)
if(text.text == ""):
     print("暂无新的消息提醒")
else:
    print(text.text) """
    
""" 
# 获取消息弹窗的未看元素
# .msgModel .layui-table-view .layui-table-box .layui-table-main table tbody input
browser.find_element_by_id('notice').click()
time.sleep(2)
inputs = browser.find_elements_by_css_selector('.msgModel table tbody input')
for input in inputs:
    print("***%s"%input)

 """

# 全屏icon
# fullScreen
fullScreen = browser.find_element_by_id('fullScreen')
# fullScreen.click()

# 该方法用来确认元素是否存在，如果存在返回flag=true，否则返回false        
def isElementExist(element):
    flag=True
    try:
        browser.find_element_by_css_selector(element)
        return flag
    
    except:
        print('没找到元素')
        flag=False
        return flag

# 退出登录
logout = browser.find_element_by_id('logout')
# logout.click()
time.sleep(2)

# 弹窗
# logoutTip = 's=>div.layui-layer-dialog a.layui-layer-btn0' 
# 退出登录弹窗
ss = '.layui-layer.layui-layer-dialog'
# logoutTip = browser.find_element_by_css_selector('.layui-layer.layui-layer-dialog')
flag = isElementExist(ss)
if flag:
    # 退出登录弹窗里的确定按钮
    logout_confirm = browser.find_element_by_css_selector('div.layui-layer-dialog a.layui-layer-btn0')
    # 退出登录弹窗里的取消按钮
    logout_cancel = browser.find_element_by_css_selector('div.layui-layer-dialog a.layui-layer-btn1')

    print(logout_confirm)
    print(logout_confirm.text)

    print(logout_cancel)
    print(logout_cancel.text)
else:
    print('没有退出登录弹窗')










