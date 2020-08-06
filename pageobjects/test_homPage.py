# -*- encoding: utf-8 -*-
"""
@Author: 黄权权
@Date: 2020-07-10 09:57:28
@LastEditors: 黄权权
@LastEditTime: 2020-07-10 16:42:50
@Descripttion:
"""
# here put the import lib

# 为了导入自定义的包，编写以下代码
import sys
import os
# __file__获取执行文件相对路径，整行为取上一级的上一级目录
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(BASE_DIR)

import time
from units.base_page import BasePage


class HomePage(BasePage):
    # ====================系统顶部元素================================================
    # 菜单切换
    menu = 'class_name=>ok-show-menu'

    # 点击：菜单显示/菜单消失
    def click_menu(self):
        self.click(self.menu)

    # 推荐使用Chrome浏览器,使用css选择器定位
    recommend = 's=>.recommend > a'

    # 点击新建窗口打开谷歌浏览器下载页面
    def click_recommend(self):
        self.click(self.recommend)

    # 刷新icon,刷新左侧某一导航的数据
    refresh = 's=>.layui-nav-item .ok-refresh'

    # 点击系统顶部刷新icon
    def click_refresh(self):
        self.click(self.refresh)

    # 消息通知icon
    notice = 'id=>notice'

    # 点击弹出消息窗口
    def click_notice(self):
        self.click(self.notice)

    # 消息数字
    notice_num = 's=>#notice > span'

    # 获取消息数字
    def get_noticeNum(self):
        time.sleep(2)  # 等待两秒避免js还没把数据写到标签内
        noticeNum = self.find_element(self.notice_num).text
        if noticeNum == "":
            print("暂无新的消息提醒")
            return 0
        return noticeNum

    # 全屏icon
    fullScreen = 'id=>fullScreen'

    # 点击全屏/取消全屏
    def click_fullScreen(self):
        self.click(self.fullScreen)

    # 退出登录
    logout = 's=>logout'

    def click_logout(self):
        self.click(self.logout)

    # 判断这个元素是否存在页面的函数，可多次调用
    def isElementExist(self, element):
        return self.isElementExist(element)

    # 退出登录提示弹窗
    logoutTip = 's=>.layui-layer.layui-layer-dialog'
    # 退出登录弹窗里的确定按钮
    logout_confirm = 's=>div.layui-layer-dialog a.layui-layer-btn0'

    def click_logout_confirm(self, element):
        isExist = self.isElementExist(self.logoutTip)
        if isExist:
            self.click(self.logout_confirm)

    # 退出登录弹窗里的取消按钮
    logout_cancel = 's=>div.layui-layer-dialog a.layui-layer-btn1'

    def click_logout_cancel(self, element):
        isExist = self.isElementExist(self.logoutTip)
        if isExist:
            self.click(self.logout_confirm)
