#coding=utf-8

import pymysql
from file_handler.ConfigReader import ConfigReader

class DBHelper:


    def testDBConnection(self):

        """test db connection"""

        db = self.connect2db()

        cursor = db.cursor()
        cursor.execute("SELECT VERSION()")
        data = cursor.fetchone()
        print ("Database version : %s " % data)
        db.close()

    def insertArticles(self, title, url, comments, thumbs):

        """存储数据"""

        db = self.connect2db()

        sqlStr = 'insert into articles (title, url, comments, thumbs) values("%s", "%s", "%d", "%d")' % (title, url, comments, thumbs)
        print(sqlStr)

        try:
            cursor = db.cursor()
            cursor.execute("SET NAMES utf8")
            cursor.execute(sqlStr)
            db.commit()
            db.close()
            print("insert successfully!!")
        except:
            print("insert failed!!")
            db.rollback()
            db.close()



    def connect2db(self):

        """连接到数据库"""

        config = ConfigReader()
        dbconfigs = config.read()

        # read by type
        db_host = dbconfigs.get('db', 'db_host')
        db_user = dbconfigs.get('db', 'db_user')
        db_port = dbconfigs.getint('db', 'db_port')
        db_pass = dbconfigs.get('db', 'db_pass')
        db_schema = dbconfigs.get('db', 'db_schema')

        db = pymysql.connect(host=db_host,user=db_user,password=db_pass,db=db_schema, port=db_port, charset="utf8" )

        return db

if __name__ == '__main__':
    dbHelper = DBHelper()
    dbHelper.testDBConnection()
