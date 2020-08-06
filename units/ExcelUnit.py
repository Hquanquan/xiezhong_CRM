# 这是自定义的，要导入使用
from logs.logger import Logger
# 创建一个logger 日志对象

# 1、读取Excel表格
# 导入与Excel操作相关的第三方库：xlrd
import xlwt
import xlrd
import requests
import json
from random import randint
import configparser
import xlutils
import os
import configparser
from xlutils.copy import copy  # 复制函数

# 创建一个logger 日志对象
logger = Logger(logger="ExcelUnit").getlog()


class ExcelUnit(object):

    # 获取config文件中的某一值
    def get_config_value(self, section, option):
        # 实例化一个 configparser 对象 config
        config = configparser.ConfigParser()
        # 获取配置文件的路径,os.path.abspath('.')返回的是当前文件的父目录
        file_path = os.path.abspath('.') + '\\config\\config.ini'
        # print("配置文件config路径==============》",file_path)
        # 读取该文件所有内容
        config.read(file_path)
        value = config.get(section, option)
        return value

    # 打开指定位置的表格，复制一份表格，并把复制的表格返回:
    # 返回值：workBookNew新复制的Excel表 ,workSheet读取Excel数据,wrSheet写入数据到Excel
    def OpenExcle(self, filepath, index=1):
        try:
            # 打开Excel表格,formatting_info=True 表示保留格式打开表格
            self.workBook = xlrd.open_workbook(filepath, formatting_info=True)
            # 选中要操作的子表，默认下标为0
            workSheet = self.workBook.sheet_by_index(index - 1)
            print(workSheet)
            # 通过sheet名称选择子表
            # workSheet1 = self.workBook.sheet_by_name('统计')
            #  print(workSheet1)
            # workSheet2 = self.workBook.sheets()[0]       #通过索引顺序获取
            # print(workSheet2)

            # 复制一份Excel表格
            workBookNew = copy(self.workBook)
            # 获取复制的Excel表格里的第一个子表，把测试结果写入复制的wrsheet
            wrSheet = workBookNew.get_sheet(0)
            print(wrSheet)
            return [workBookNew, workSheet, wrSheet]
        except Exception as e:
            print(e)
            logger.error(e)

    # 读取workSheet表格里第readRow行第readColumn列的数据
    def readExcleSheet(self, sheet, readRow, readColumn):
        return sheet.cell_value(readRow, readColumn)  # 第readRow行第readColumn列的数据,输入参数单元格

    # 为指定的sheet表在第row行第column列写入数据date
    def writeExcleSheet(self, sheet, writeRow, writeColummn, date):
        # 要先对date数据进行格式化json.dumps(date,ensure_ascii=False)
        sheet.write(writeRow, writeColummn, date)
        return sheet

    # 返回当前时间的字符串,用来为文件命名
    def fileName_of_Time(self):
        # 导入时间函数库
        from datetime import datetime
        import time
        # # 获取当前时间并赋值给mytoday
        # myToday = datetime.date.today()
        # # 当天的日期格化为字符串
        # myTodayStr =myToday.strftime('%Y-%m-%d')

        # 获取当前时间点作为截屏的图片名称
        # rq = time.strftime('%Y%m%d%H%M',time.localtime(time.time()))

        # 当前具体时间格式化为字符串
        strtime = datetime.now().strftime('%Y-%m-%d_%H_%M_%S')
        return strtime

    # 保存Excle文件到指定的位置,格式为：.xls
    def saveExcle(self, excle, filepath):
        excle.save(filepath)


if __name__ == '__main__':

    testExcelUnit = ExcelUnit()
    filepath = 'E:\\Python\\前程无忧-搜索结果-2020-04-30.xls'

    SaveExcelPath = testExcelUnit.get_config_value("ExcelFile", "SaveExcelPath")

    print(SaveExcelPath)

    lists = testExcelUnit.OpenExcle(filepath)

    row = testExcelUnit.get_config_value("ReadTestCase", "readRow")
    column = testExcelUnit.get_config_value("ReadTestCase", "readColumn")
    # 取出来的数据一定要转换一下格式
    aa = testExcelUnit.readExcleSheet(lists[1], int(row) - 1, int(column) - 1)
    print(aa)
    #
    for one in range(1, 11):
        cellDate = testExcelUnit.readExcleSheet(lists[1], one, int(column) - 1)
        print(cellDate)
        testExcelUnit.writeExcleSheet(lists[2], one, 9, cellDate)

    file1 = SaveExcelPath + testExcelUnit.fileName_of_Time() + '.xls'
    print(file1)
    testExcelUnit.saveExcle(lists[0], file1)
    print('================================================')
