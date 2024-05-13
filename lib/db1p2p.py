#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/4/19 
# Author    : smart
# @File     : p2p.py
# @Software : PyCharm
import pymysql
import sys
sys.path.append('..')
from config.config import *
# 建立数据库的连接
def conn():
    conn=pymysql.connect(
                         host="localhost",
                         user='root',password='root',
                         db='p2p',port=3306
                        ,charset='utf8'
    )
    return conn
#封装数据库的查询数据
def query_p2p(sql):
    # 建立连接
    con=conn()
    # 建立游标
    cur=con.cursor()
    # 执行sql
    cur.execute(sql)
    # 获取返回的查询结果
    result=cur.fetchone()
    return result
# 封装数据库的更改操作
def change_p2p(sql):
    # 建立连接
    con=conn()
    # 建立游标
    cur = con.cursor()
    try:
        # 执行sql
        cur.execute(sql)
#         提交更改
        con.commit()
    except Exception as e:
        # 回滚
        con.rollback()
    #     获取返回的查询结果
    finally:
        # 关闭游标
        cur.close()
        # 关闭连接
        con.close()
#     封装常用的数据库操作
def check_p2p(proNum):
    sql="select * from product where proNum ='{}'".format(proNum)
    result = query_p2p(sql)
    return True if result else False
# 添加
def add_p2p(bh,name,qx,nh):
    sql="insert into product(proNum,proName,proLimit,annualized)values ('{}','{}','{}','{}').".format(bh,name,qx,nh)
    change_p2p(sql)
#删除
def del_p2p(proNum):
    sql="delete from product where proNum='{}'".format(proNum)
    change_p2p(sql)
