# coding=utf-8
"""
excel 读写
支持 xls， xlsx, csv 格式
"""

import xlrd
import xlwt
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

    def input(self):

        """根据输入提前判断是否继续下一步"""

        str = raw_input("Input file: ")

        if str.lower() == 'stop':
            sys.exit()
        else:
            if os.path.exists(str):
                excelHandler.route(str)
            else:
                print('找不到文件 %s , 请重试！' % str)
                # sys.exit()
                # a = raw_input("Input file: ")
                self.input()


    def writeSheetRow(self, sheet, rowValueList, rowIndex):

        """写行数据到sheet"""

        i = 0
        for sValue in rowValueList:
            strValue = unicode(str(sValue), 'utf-8')
            sheet.write(rowIndex, i, strValue)
            i = i + 1


    def saveExcel(self, filename):

        """保存数据到excel"""

        wbk = xlwt.Workbook()
        sheet = wbk.add_sheet('sheet1', cell_overwrite_ok=True)
        headList = ['标题1', '标题2', '标题3', '标题4', '总计']
        rowIndex = 0
        self.writeSheetRow(sheet, headList, rowIndex)
        for i in range(1, 11):
            rowIndex = rowIndex + 1
            valueList = []
            for j in range(1,5):
                valueList.append(j*i)
            self.writeSheetRow(sheet, valueList, rowIndex)

        wbk.save(filename)

    def saveCSV(self, filename):

        """保存数据到csv文件"""



if __name__ == '__main__':

    excelHandler = ExcelHandler()
    # filename = raw_input("Input file: ")
    #excelHandler.input()
    excelHandler.saveExcel('test_write_excel.xls')



