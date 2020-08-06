# 日志类，用于打印操作日志

# 导入相关模块
# 日志模块
import logging
# 操作系统文件模块
import os.path
# 时间模块
import time


class Logger(object):

    def getlog(self):
        return self.logger

    # 初始化
    def __init__(self, logger):
        # 创建一个 logger 对象
        self.logger = logging.getLogger(logger)  # logger 对象为被执行的对象类
        self.logger.setLevel(logging.DEBUG)  # 设置日志模式为调试模式

        # 设置时间格式
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        # 设置日志的存储路径
        log_path = os.path.abspath('..') + '\\log\\'

        # 判断log文件夹是否被创建，未创建则进行创建
        isExists = os.path.exists(log_path)  # 存在返回Ture,不存在返回False
        if not isExists:  # Ture就变成False，不执行，反之则执行
            try:
                # 创建这个路径的文件夹
                os.makedirs(log_path)
            except Exception as e:
                print('创建文件夹失败！原因：', e)

        # log日志的名称以时间来命名
        log_name = log_path + rq + '.log'
        # 创建一个 handler，用于写入日志文件,注意一定要指定编码格式encoding='utf-8'
        fh = logging.FileHandler(log_name, encoding='utf-8')
        fh.setLevel(logging.INFO)

        # 再创建一个handler ,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 给logger 添加 handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)
