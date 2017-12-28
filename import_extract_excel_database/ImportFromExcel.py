# coding=utf-8

"""
从excel读取数据并将其写入数据库
"""

from file_handler.ExcelHandler import ExcelHandler
from database_handler.DBHelper import DBHelper

class ImportFromExcelHandler:

    def load2db(self, filename):

        excelHandler = ExcelHandler()
        content = excelHandler.readExcelForDB(filename)

        for c in content:
            for i in range(0, len(c)):
                article_name = c[1]
                article_url = c[2]
                dbhelper = DBHelper()
                dbhelper.insertArticles(article_name, article_url, 1, 1)


if __name__ == '__main__':
    handler = ImportFromExcelHandler()
    handler.load2db('test_extract_db_excel.xls')