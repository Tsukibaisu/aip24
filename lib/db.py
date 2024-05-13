#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/4/19 
# Author    : smart
# @File     : pip24.py
# @Software : PyCharm
import logging

import pymysql
from config.config import *
# 建立数据库的连接
def conn():
    conn=pymysql.connect(
                         host=db_host,
                         user=db_user,password=db_password,
                         db=db,port=db_port
                        ,charset='utf8'
    )
    return conn
#封装数据库的查询数据
def query_db(sql):
    # 建立连接
    con=conn()
    # 建立游标
    cur=con.cursor()
    # 在日志中打印sql语句
    logging.debug(sql)
    # 执行sql
    cur.execute(sql)
    # 获取返回的查询结果
    result=cur.fetchone()
    # 将获取的查询结果在日志中打印
    logging.debug(result)
    return result
# 封装数据库的更改操作
def change_db(sql):
    # 建立连接
    con=conn()
    # 建立游标
    cur = con.cursor()
    # 在日志中打印sql语句
    logging.debug(sql)
    try:
        # 执行sql
        cur.execute(sql)
#         提交更改
        con.commit()
    except Exception as e:
        # 将报错的信息在日志中打印
        logging.error(str(e))
        # 回滚
        con.rollback()
    #     获取返回的查询结果
    finally:
        # 关闭游标
        cur.close()
        # 关闭连接
        con.close()
#     封装常用的数据库操作
def check_user(name):
    sql="select * from t_user where user_name ='{}'".format(name)
    result = query_db(sql)
    return True if result else False
# 添加
def add_user(name,password):
    sql="insert into t_user(user_name,password)values ('{}','{}').".format(name,password)
    change_db(sql)
#删除
def del_user(name):
    sql="delete from t_user where user_name='{}'".format(name)
    change_db(sql)
