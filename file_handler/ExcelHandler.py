# coding=gbk

import xlrd

data = xlrd.open_workbook('fruits.xls')

#table = data.sheet_by_index(0) #ͨ������˳���ȡ

table = data.sheet_by_name(u"������1")

rows = table.nrows #��ȡ����
cols = table.ncols #��ȡ����

for row in range(rows):
    for i in range(len(table.row_values(row))):
        print(table.row_values(row)[i])


'''
class ExcelHandler:
    """
    excel ��д����
    """



    def read(self):
        """��ȡexcel����"""
        return False

    def write(self):
        """д������"""
        return False

'''