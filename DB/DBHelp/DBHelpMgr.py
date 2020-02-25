#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# XRLAM("DBHelpMgr")
#===============================================================================
# 注释
#===============================================================================
import pymysql

from Define import Define


def get_don_connection():
    con = pymysql.connect(host=Define.IP, user=Define.USER, password=Define.PASSWORD, database="don", \
                          port=Define.PORT, charset="utf8", use_unicode=False)
    return con

def get_don2_connection():
    con = pymysql.connect(host=Define.IP, user=Define.USER, password=Define.PASSWORD, database="don2", \
                          port=Define.PORT, charset="utf8", use_unicode=False)
    return con


def get_database_connection(database_name):
    con = pymysql.connect(host=Define.IP, user=Define.USER, password=Define.PASSWORD, database=database_name, \
                          port=Define.PORT, charset="utf8", use_unicode=False)
    return con