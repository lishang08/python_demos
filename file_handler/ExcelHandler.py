# coding=utf-8
"""
excel 读写
支持 xls， xlsx, csv 格式
"""

import xlrd
import csv
import os.path
from StringUtil import StringUtil
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class ExcelHandler:

    def readExcel(self, filename):

        """读取excel"""

        excel = xlrd.open_workbook(filename)
        ts = len(excel.sheets())
        for i in range(0, ts):
            sheet = excel.sheet_by_index(i)
            print(u'当前处理表格: %s ' % sheet.name)

            rows = sheet.nrows  # 获取行数
            cols = sheet.ncols  # 获取列数
            for i in range(rows):
                if i == 0:
                    continue # 去掉第一行
                row_content = ""
                for j in range(cols):
                    dataType = sheet.cell(i, j).ctype  # 格式化date
                    if dataType == 3:
                        util = StringUtil()
                        row_content = row_content+'|'+str(util.formatDate(sheet.cell_value(i, j), dataType))
                    else:
                        row_content = row_content+'|'+str(sheet.cell_value(i, j))
                print(row_content)

                print("--------------")

            print("=============")

    def readCSV(self, filename):

        """读取csv文件"""

        csvData = csv.reader(file(filename, 'rb'), dialect='excel') # 注意要加上dialect

        for row in csvData:
            print(row)


    def route(self, filename):

        """判断文件格式，只允许xls, xlsx, csv 格式"""

        fileSuffix = os.path.splitext(filename)[1].lower()
        print("Current input file suffix is : %s" % fileSuffix)

        if fileSuffix == '.xls' or fileSuffix == '.xlsx':
            self.readExcel(filename)
        elif fileSuffix == '.csv':
            self.readCSV(filename)
        else:
            print('Only support excel format')

    def input(self, str):

        """根据输入提前判断是否继续下一步"""

        if str.lower() == 'stop':
            sys.exit()
        else:
            if os.path.exists(filename):
                excelHandler.route(filename)
            else:
                print('找不到文件 %s , 请重试！' % filename)
                sys.exit()



if __name__ == '__main__':

    excelHandler = ExcelHandler()
    filename = raw_input("Input file: ")
    excelHandler.input(filename)



