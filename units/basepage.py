"""
    二次封装 selenium 类,又称之为通用类。用于给页面类使用
"""
# 为了导入自定义的包
import os
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains

from logs.logger import Logger

# # __file__获取执行文件相对路径，整行为取上一级的上一级目录
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(BASE_DIR)

# 声明一个Logger实例化对象 logger,用于记录日志
logger = Logger(logger="BasePage").getlog()


class BasePage(object):
    # 初始化 driver 对象
    def __init__(self, driver):
        self.driver = driver

    # 关闭浏览器
    def quit_browser(self):
        self.driver.quit()

    # forward browser 浏览器前进的方法
    def forward_browser(self):
        self.driver.forward()
        logger.info('Click forward on current page!')

    # back browser 浏览器后退的方法
    def back_browser(self):
        self.driver.back()
        logger.info('Click back to current page!')

    # close browser 关闭当前浏览器窗口
    def close_browser(self):
        try:
            self.driver.close()
            logger.info('Close and quit the browser')
        except NameError as e:
            logger.error('Failed to quit the browser with %s ' % e)

    # 截屏保存图片
    def get_windows_img(self):
        file_path = os.path.abspath('.') + '\\screenshots\\'
        # 判断文件夹是否存在，不存在则创建
        isExists = os.path.exists(file_path)  # True 就是存在，False就是不存在
        # 取反进行判断：
        if not isExists:
            try:
                os.makedirs(file_path)
            except Exception as e:
                logger.error('Failed new bulid folder %s ' % e)
                print(e)
        # 获取当前时间点作为截屏的图片名称
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        # 截屏图片的完整路径名
        screen_name = file_path + rq + '.png'

        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info('Had take screenshot and save to folder : \\screenshots')
        except Exception as e:
            logger.error('Failed to take screenshot! %s ' % e)
            print(e)
            self.get_windows_img()

    # Text input文本框输入
    def send_keys(self, selector, text):
        # 获取元素定位信息
        el = self.find_element(selector)
        el.clear()  # 清空文本框
        try:
            # 输入文本
            el.send_keys(text)
            logger.info("Had type \' %s \' in inputBox" % text)
        except NameError as e:
            logger.error("Failed to type in inputBox with %s" % e)
            self.get_windows_img()

    # 清空文本输入框
    def clear(self, selector):
        el = self.find_element(selector)
        try:
            el.clear()
            logger.info("Clear text in input box before type")
        except NameError as e:
            logger.error("Failed to cleat text in input box wirh %s" % e)
            self.get_windows_img()

    # 点击事件
    def click(self, selector):
        el = self.find_element(selector)
        # print(el)
        try:
            el.click()
            logger("The element was clicked!")
        except NameError as e:
            logger.error("Failed to click the element! %s " % e)
            self.get_windows_img()

    # 获取网页标题
    def get_url_title(self):
        logger.info("Current page title is %s" % self.driver.title)
        return self.driver.title

        # find_element_**  元素定位方法  selector:元素位置

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

    # 鼠标悬停在元素上

    # 鼠标移到某个元素上
    def move_to_element(self, selector):
        el = self.find_element(selector)  # 获取元素位置信息
        try:
            ActionChains(self.driver).move_to_element(el).perform()
            logger.info("The mouse move on %s" % el.text)
        except NameError as e:
            logger.error("Failed to the mouse move on %s " % e)
            self.driver.get_windows_img()
