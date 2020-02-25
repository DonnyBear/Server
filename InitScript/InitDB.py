#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# XRLAM("InitDB")
#===============================================================================
# 注释
#===============================================================================
import pymysql

class table_base(object):
    SQL = ""

    @classmethod
    def execute(cls, cursor):
        cursor.execute(cls.SQL)

class user(table_base):
    SQL = "create table user(id INT(11), name VARCHAR(20));"
    DATABASE = 'don'

class item(table_base):
    SQL = "create table item(id INT(11), name VARCHAR(20));"
    DATABASE = 'don2'




if __name__ == "__main__":
    pass