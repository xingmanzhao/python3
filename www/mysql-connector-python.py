#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

__AUTHOR__ = 'xingman zhao'

import mysql.connector

conn = mysql.connector.connect(user='root',password='',database='test')
cursor = conn.cursor()
cursor.execute('insert into user values(%s,%s)',['1','xingman'])
print(cursor.rowcount)
cursor.close()

cursor = conn.cursor()
cursor.execute('select * from user')
print(cursor.fetchall())
cursor.close()
