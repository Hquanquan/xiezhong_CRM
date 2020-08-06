# 创建一个浏览器的类

# 导入相关的库
import configparser
# 为了导入自定义的包
import os

from selenium import webdriver

# __file__获取执行文件相对路径，整行为取上一级的上一级目录
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(BASE_DIR)
# 这是自定义的，要导入使用
from logs.logger import Logger

# 创建一个logger 日志对象
logger = Logger(logger="Browser").getlog()


class Browser(object):
    def __init__(self, driver):
        self.driver = driver

    # 打开浏览器的方法
    def open_browser(self, driver):
        # 1、读取配置文件的信息，打开相应的浏览器
        # 实例化一个 configparser 对象 config
        config = configparser.ConfigParser()
        # 获取配置文件的路径,os.path.abspath('.') 返回的是当前文件的父目录
        print('当前文件的父目录:%s' % os.path.abspath('.'))
        # os.path.abspath('..')  #获取当前文件的父目录的父目录
        print('当前文件的父目录的父目录:%s' % os.path.abspath('..'))
        file_path = os.path.abspath('..') + '\\config\\config.ini'
        print("配置文件config路径==============》", file_path)
        # 读取该文件所有内容
        config.read(file_path, encoding='utf-8')
        # 读取浏览器类型信息,并打印日志
        browser = config.get("browserType", "browserName")
        logger.info("You had select %s browser!" % browser)
        # 读取URl地址信息,并打印日志
        url = config.get("testServer", 'URL')
        logger.info("The test server url is %s" % url)

        # 判断使用什么浏览器，获取浏览器实例
        if browser == 'FireFox':
            # firefox火狐浏览器的驱动已安装在浏览器上，直接调用即可
            driver = webdriver.Firefox()
            logger.info('Starting firefox browser!')
        elif browser == 'Chrome':
            # 谷歌浏览器的驱动，在这个文件夹，需要定位到这里
            driver = webdriver.Chrome(r'E:\Python\chromedriver_win32\chromedriver.exe')
            logger.info('Starting Chorme browser!')
        elif browser == 'IE':
            driver = webdriver.Ie()
            logger.info('Starting IE browser!')

        # 利用获取到的briver 打开浏览器，访问url地址,使用try 语句
        try:
            driver.get(url)
            logger.info("Open url %s " % url)
            # 等待10秒
            driver.implicitly_wait(10)
            logger.info("Set implicitly wait 10")
            # 窗口最大化
            driver.maximize_window()
            # 返回driver实例化对象
            return driver
        except Exception as e:
            print(e)
            logger.info(e)

    # 关闭浏览器
    def quit_browser(self):
        logger.info('Now,Close and quit the browser!')
        print(self.driver)
        self.driver.quit()
