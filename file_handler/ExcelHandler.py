# coding=utf-8
"""
excel 读写
支持 xls， xlsx 格式
"""

import xlrd
from StringUtil import StringUtil

class ExcelHandler:

    def readExcel(self, filename):
        excel = xlrd.open_workbook(filename)
        ts = len(excel.sheets())
        for i in range(0, ts):
            sheet = excel.sheet_by_index(i)
            print(u'当前处理: %s ' % sheet.name)

            rows = sheet.nrows  # 获取行数
            cols = sheet.ncols  # 获取列数
            for i in range(rows):
                for j in range(cols):
                    #格式化date
                    dataType = sheet.cell(i, j).ctype
                    if dataType == 3:
                        util = StringUtil()
                        print(util.formatDate(sheet.cell_value(i, j), dataType))
                    else:
                        print(sheet.cell_value(i, j))

                print("--------------")

            print("=============")



if __name__ == '__main__':

    excelHandler = ExcelHandler()
    excelHandler.readExcel('management.xls')



