# coding=gbk

"""从数据库读取数据到excel"""
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from database_handler.DBHelper import DBHelper
from file_handler.ExcelHandler import ExcelHandler

class Extract2Execel:

    def extract(self):

        dbhelper = DBHelper()
        db = dbhelper.connect2db()
        cursor = db.cursor()
        cursor.execute("select * from articles")
        articles = cursor.fetchall()

        excelHandler = ExcelHandler()

        excelHandler.saveDBData2Excel(articles, 'test_extract_db_excel.xls')


if __name__ == '__main__':
    handler = Extract2Execel()
    handler.extract()