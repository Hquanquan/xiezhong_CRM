# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
    二次封装 selenium 类,又称之为通用类。用于给页面类使用
"""

# 为了导入自定义的包
# __file__获取执行文件相对路径，整行为取上一级的上一级目录
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(BASE_DIR)

import os
import time

from selenium.common.exceptions import NoSuchElementException
# 导入selenium中的actionchains的方法
from selenium.webdriver.common.action_chains import ActionChains

from logs.logger import Logger

# 引用自定义日志文件
logger = Logger(logger="BasePage").getlog()


class BasePage(object):

    # 初始化 driver 对象
    def __init__(self, driver):
        self.driver = driver

    # quit browser and end testing 浏览器退出方法
    def quit_browser(self):
        self.driver.quit()

    # forward browser 浏览器前进方法
    def forward_browser(self):
        self.driver.forward()
        logger.info("Click forward on current page.")

    # back browser 浏览器后退方法
    def back_browser(self):
        self.driver.back()
        logger.info("Click back to current page.")

    # close_browser 关闭当前浏览器窗口
    def close_browser(self):
        try:
            self.driver.close()
            logger.info("Close and quit the browser")
        except NameError as e:
            logger.error("Failed to quit the browser with %s" % e)

    # 保存图片
    def get_windows_img(self):
        file_path = os.path.abspath('..') + '/screenshots/'
        isExists = os.path.exists(file_path)
        # 判断文件夹是否存在，如果不存在则创建。
        if not isExists:
            try:
                os.makedirs(file_path)
            except Exception as e:
                logger.error("Failed new bulid folder %s" % e)
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("Had take screenshot and save to folder : /screenshots")
        except NameError as e:
            logger.error("Failed to take screenshot! %s" % e)
            self.get_windows_img()

    # find_element_**  一个元素定位方法  selector:元素位置
    def find_element(self, selector):
        """
        这个地方为什么是根据=>来切割字符串，请看页面里定位元素的方法
        submit_btn = "id=>su"
        login_lnk = "xpath => //*[@id='u1']/a[7]"  # 百度首页登录链接定位
        如果采用等号，结果很多xpath表达式中包含一个=，这样会造成切割不准确，影响元素定位
        :param selector:
        :return:
        """
        element = ''

        if '=>' not in selector:
            return self.driver.find_element_by_id(selector)

        selector_by = selector.split('=>')[0]  # 元素名称
        selector_value = selector.split('=>')[1]  # 元素ID名称

        if selector_by == "i" or selector_by == "id":
            try:
                element = self.driver.find_element_by_id(selector_value)  # id 定位
                logger.info("Had find the element \' %s \' successful"
                            "by %s via value:%s" % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException:%s" % e)
                self.get_windows_img()
        elif selector_by == "n" or selector_by == "name":
            element = self.driver.find_element_by_name(selector_value)  # name 名称定位

        elif selector_by == "c" or selector_by == "class_name":
            element = self.driver.find_element_by_class_name(selector_value)  # css 样式名称定位

        elif selector_by == "l" or selector_by == "link_text":
            try:
                element = self.driver.find_element_by_link_text(selector_value)  # 文本超链接定位
                logger.info(("Had find the element \' %s \' successful"
                             "by %s via value:%s" % (element.text, selector_by, selector_value)))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException:%s" % e)
                self.get_windows_img()

        elif selector_by == "p" or selector_by == "partial_link_text":
            element = self.driver.find_element_by_partial_link_text(selector_value)

        elif selector_by == "t" or selector_by == "tag_name":
            element = self.driver.find_element_by_tag_name(selector_value)

        elif selector_by == "x" or selector_by == "xpath":
            try:
                element = self.driver.find_element_by_xpath(selector_value)
                logger.info("Had find the element \' %s \' successful"
                            "by %s via value:%s" % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException:%s" % e)
                self.get_windows_img()

        elif selector_by == "s" or selector_by == "selector_selector":
            element = self.driver.find_element_by_css_selector(selector_value)

        else:
            logger.error("Please enter a valid type of targeting elements.")
            raise NameError("Please enter a valid type of targeting elements.")

        return element

    # Text input 文本框输入
    def send_keys(self, selector, text):
        el = self.find_element(selector)  # 获取元素位置信息
        el.clear()  # 文本框清空
        try:
            el.send_keys(text)  # 输入文本信息
            logger.info("Had type \' %s \' in inputBox" % text)
        except NameError as e:
            logger.error("Failed to type in input box with %s" % e)
            self.get_windows_img()

    # Text clear 文本框清空 selector:元素位置
    def clear(self, selector):
        el = self.find_element(selector)  # 获取元素位置信息
        try:
            el.clear()
            logger.info("Clear text in input box before type")
        except NameError as e:
            logger.error("Failed to type in input box with %s" % e)
            self.get_windows_img()

    # Text click 点击事件 selector:元素位置
    def click(self, selector):
        el = self.find_element(selector)  # 获取元素位置信息
        print(el)
        try:
            el.click()
            print(el)
            logger.info("The emement was click")  # 并不是每个元素都存在 text 属性
        except NameError as e:
            logger.error("Failed to type in input box with %s" % e)
            self.get_windows_img()

    # get_url_title 获取网页标题
    def get_url_title(self):
        logger.info("Current page title is %s" % self.driver.title)
        return self.driver.title

    # 鼠标悬停在元素上
    def move_to_element(self, selector):
        el = self.find_element(selector)  # 获取元素位置信息
        try:
            ActionChains(self.driver).move_to_element(el).perform()
            logger.info("The mouse move on %s" % el.text)
        except NameError as e:
            logger.error("Failed to the mouse move on %s " % e)
            self.driver.get_windows_img()

    # 获取当前窗口
    def current_window_handle(self):
        return self.driver.current_window_handle

    # 获取所有窗口
    def window_handles(self):
        return self.driver.window_handles

    # 切换窗口
    def switch_to_window(self, window=""):
        if window == "":
            self.driver.switch_to_window(self.current_window_handle())
        else:
            self.driver.switch_to_window(window)

    # 切换到当前最新打开的窗口
    def switch_to_new_window(self):
        self.driver.switch_to.window(self.window_handles()[-1])

    # 刷新当前页面
    def refresh(self):
        self.driver.refresh()

    # 切换到弹窗窗口
    def switch_to_alert(self):
        return self.driver.switch_to.alert()

    # 同步z执行js脚本:execute_script为同步执行且执行时间较短。
    # WebDriver会等待同步执行的结果然后执行后续代码；
    def execute_script(self, js):
        return self.driver.execute_script(js)

    # 异步执行js脚本:execute_async_script为异步执行且执行时间较长。
    # WebDriver不会等待异步执行的结果，而是直接执行后续的代码
    def execute_async_script(self, js):
        return self.driver.execute_async_script(js)

    # 找到一组元素
    def find_elements(self, selector):
        elements = ''

        if '=>' not in selector:
            return self.driver.find_elements_by_id(selector)

        selector_by = selector.split('=>')[0]  # 元素名称
        selector_value = selector.split('=>')[1]  # 元素ID名称

        if selector_by == "i" or selector_by == "id":
            try:
                elements = self.driver.find_elements_by_id(selector_value)  # id 定位
                logger.info("Had find the elements \' %s \' successful"
                            "by %s via value:%s" % (elements, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException:%s" % e)
                self.get_windows_img()

        elif selector_by == "n" or selector_by == "name":
            elements = self.driver.find_elements_by_name(selector_value)  # name 名称定位

        elif selector_by == "c" or selector_by == "class_name":
            elements = self.driver.find_elements_by_class_name(selector_value)  # className名称定位

        elif selector_by == "l" or selector_by == "link_text":
            try:
                elements = self.driver.find_elements_by_link_text(selector_value)  # 文本超链接定位
                logger.info(("Had find the elements \' %s \' successful"
                             "by %s via value:%s" % (elements, selector_by, selector_value)))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException:%s" % e)
                self.get_windows_img()

        elif selector_by == "p" or selector_by == "partial_link_text":
            elements = self.driver.find_elements_by_partial_link_text(selector_value)

        elif selector_by == "t" or selector_by == "tag_name":
            elements = self.driver.find_elements_by_tag_name(selector_value)

        elif selector_by == "x" or selector_by == "xpath":
            try:
                elements = self.driver.find_elements_by_xpath(selector_value)
                logger.info("Had find the elements \' %s \' successful"
                            "by %s via value:%s" % (elements, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException:%s" % e)
                self.get_windows_img()

        elif selector_by == "s" or selector_by == "selector_selector":
            elements = self.driver.find_elements_by_css_selector(selector_value)

        else:
            logger.error("Please enter a valid type of targeting elements.")
            raise NameError("Please enter a valid type of targeting elements.")

        return elements

    # 获取sessionid
    def get_sessionid(self):
        # 是要从localStorage中获取还是要从sessionStorage中获取，具体看目标系统存到哪个中
        # window.sessionStorage和直接写sessionStorage是等效的
        # 一定要使用return，不然获取到的一直是None
        # get的Item不一定就叫sessionId，得具体看目标系统把sessionid存到哪个变量中
        sessionid = self.driver.execute_script('return sessionStorage.getItem("sessionId");')

        # 另外sessionid一般都直接通过返回Set-Cookies头设置到Cookie中，所以也可以从Cookie读取
        # 获取浏览器所有Set-Cookie，返回对象是字典列表
        # cookies = self.driver.get_cookies()
        # 获取单项Cookie，是不是叫sessionId取决于系统存成什么变量，单项Cookie是字典
        # cookie = self.driver.get_cookie("sessionId")
        # cookie = cookie["value"]
        # print(f"{cookies}")
        return sessionid

    # 获取token
    def get_token(self):
        # 是要从localStorage中获取还是要从sessionStorage中获取，具体看目标系统存到哪个中
        # window.sessionStorage和直接写sessionStorage是等效的
        # 一定要使用return，不然获取到的一直是None
        # get的Item不一定就叫token，得具体看目标系统把token存到哪个变量中
        token = self.driver.execute_script('return sessionStorage.getItem("token");')
        # print(f"{token}")
        return token

    # 判断当前元素是否可见display
    def isdispaly(self):
        return self.driver.isdispaly()

    # 滑动滚动条，到达指定的元素
    def slidingScrollbar(self, target):
        js = "arguments[0].scrollIntoView();"
        self.driver.execute_script(js, target)

    # 该方法用来确认元素是否存在，如果存在返回flag = true，否则返回false
    def isElementExist(self, element):
        flag = True
        try:
            ele = self.find_element(element)
            logger.info("the elements %s is exist!" % ele)
        except:
            flag = False
            logger.info("该元素没有被找到，不存在页面中")
        return flag

    # 获取元素标签内的内容
    def get_text(self, selector):
        el = self.find_element(selector)  # 获取元素位置信息
        return el.text
