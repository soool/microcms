# -*- coding: utf-8 -*- 
import MySQLdb
import os, sys

class Db(object):
    # 初始化数据参数（后续可以考虑用配置文件的方式）
    def __init__(self):
        self.__host = 'localhost'
        self.__db = 'microcms'
        self.__user = 'root'
        self.__passwd = 'root'

    # 获取数据库连接
    def __getDbConn(self):
        self.__conn = MySQLdb.connect(
            host = self.__host,
            db = self.__db,
            user = self.__user,
            passwd = self.__passwd
        )
        self.__conn.autocommit(True)

    # 写入数据
    def insertData(self, item):
        # item {'name': 'root', 'passwd': 'root'}
        try:
            self.__getDbConn()
            self.__cursor = self.__conn.cursor()
            # SQL 参数
            sql = "INSERT INTO users (uname, upasswd) VALUES (%s, %s)"
            params = (item['name'], item['passwd'])

            # SQL执行
            return self.__cursor.execute(sql, params)
        finally:
            self.__cursor and self.__cursor.close()
            self.__conn and self.__conn.close()

    # 获取数据
    def getData(self, rows):
        # rows: int 行数
        try:
            self.__getDbConn()

            # SQL query
            sql = 'SELECT * FROM users LIMIT %s' % rows

            # SQL执行
            self.__cursor = self.__conn.cursor()
            self.__cursor.execute(sql)

            # 返回数据
            return self.__cursor.fetchall()
        finally:
            self.__cursor and self.__cursor.close()
            self.__conn and self.__conn.close()

mydb = Db()
print mydb.getData(1)
print mydb.getData(2)

#print mydb.insertData({'name': 'gresic', 'passwd': 'gresic'})
print mydb.getData(4)
