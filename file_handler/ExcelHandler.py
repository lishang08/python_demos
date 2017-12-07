# coding=gbk

import xlrd

data = xlrd.open_workbook('fruits.xls')

#table = data.sheet_by_index(0) #通过索引顺序获取

table = data.sheet_by_name(u"工作表1")

rows = table.nrows #获取行数
cols = table.ncols #获取列数

for row in range(rows):
    for i in range(len(table.row_values(row))):
        print(table.row_values(row)[i])


'''
class ExcelHandler:
    """
    excel 读写操作
    """



    def read(self):
        """读取excel数据"""
        return False

    def write(self):
        """写入数据"""
        return False

'''