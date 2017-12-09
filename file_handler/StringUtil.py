# coding=utf-8

"""
工具类
处理excel string，根据ctype判断string是属于那种类型
ctype： 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error

"""
from datetime import datetime
from xlrd import xldate_as_tuple

class StringUtil:

    def formatDate(self, value, ctype):

        if ctype == 3:
            date = datetime(*xldate_as_tuple(value, 0))
            cell = date.strftime('%Y/%d/%m %H:%M:%S')

        return cell


if __name__ == '__main__':
    stringUtil = StringUtil()
    print(stringUtil.formatDate(41821.0, 3))