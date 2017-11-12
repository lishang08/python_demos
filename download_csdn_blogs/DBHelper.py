#coding=utf-8

import pymysql

class DBHelper:


    def testDBConnection(self):
        """test db connection"""
        db = pymysql.connect(host="localhost",user="root",password="Abcd1234",db="python", port="3306", charset="utf8" )
        cursor = db.cursor()
        cursor.execute("SELECT VERSION()")
        data = cursor.fetchone()
        print ("Database version : %s " % data)
        db.close()

    def insertArticles(self, title, url, comments, thumbs):
        """store new article to database"""
        db = pymysql.connect(host="localhost",user="root",password="Abcd1234",db="python", port=3306, charset="utf8" )
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

if __name__ == '__main__':
    dbHelper = DBHelper()
    dbHelper.testDBConnection()
