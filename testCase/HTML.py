"""
@Author: 黄权权
@Date: 2020-07-07 19:39:20
@LastEditors: 黄权权
@LastEditTime: 2020-07-08 18:07:39
@Descripttion:
"""

# 1、导入相关的模块
import unittest
import HTMLTestRunner
import os
import time
from datetime import date
from test_login import Login

# 保存文件的设置
# 获取当天日期
now = date.today()
# 格式化日期
dateStr = now.strftime('%Y-%m-%d')  # 2020-10-10
rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))  # 202007081012
# 获取当前运行文件的上一级目录
dir = os.path.abspath('.')

# 2、加载被测模块里的测试类
search_test = unittest.TestLoader().loadTestsFromTestCase(Login)

# 3、添加被测模块到unittest.TestSuite([a,b]),以数组的形式传参
smoke_tests = unittest.TestSuite(search_test)
#  4、TestRunner运行测试
# unittest.TextTestRunner(verbosity=2).run(smoke_tests)
# 使用HTMLTestRunner代替默认的unittest.TextTestRunner()执行测试用例即可
#  5、写入测试结果
# 创建保存文件的路径
# filepath = dir + "\\test_reports\\SmokeTestReport{}.html".format(dateStr)
filepath = dir + "\\test_reports\\SmokeTestReport{}.html".format(rq)

print(filepath)
with open(filepath, 'wb') as outfile:
    runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title='标题：冒烟测试', description='')
    runner.run(smoke_tests)
