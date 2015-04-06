# -*- coding:utf-8 -*-
import MySQLdb
import os, sys

# 连接数据库
try:
    conn = MySQLdb.connect(host='localhost', user='root', passwd='root')
except Exception, e:
    print e
    sys.exit()

conn.select_db('microcms')

# 获取cursor对象
cursor = conn.cursor()

# 创建用户表users
sql = "create table if not exists users(uid int not null auto_increment primary key, uname char(50) not null, upasswd char(50) not null)"
try:
    cursor.execute(sql)
except Exception, e:
    print e
    sys.exit()

# 插入数据
sql = "insert into users(uname, upasswd) values (%s, %s)"
val = (('root', 'root'), ('oless', '8080'), ('merge', '5000'))
try:
    print 'bug'
    print  cursor.executemany(sql, val)
except Exception, e:
    print e
    sys.exit()

# 关闭数据库及其连接
conn.commit()
cursor.close()
conn.close()
