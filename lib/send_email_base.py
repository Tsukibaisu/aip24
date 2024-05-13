#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/4/27 
# Author    : smart
# @File     : send_email_base.py
# @Software : PyCharm
# 连接邮箱
import smtplib
# 发邮件
from email.mime.text import MIMEText
# 发送的对象
msg=MIMEText('邮件的内容','plail','utf_8')
# 发件人
msg['From']='dan.ai.ta.ya@qq.com'
# 收件人
msg['To']='dan.ai.ta.ya@qq.com'
# 邮件主题
msg['Subject']='测试报告主题'
# 创建一个stmp的链接
smtp= smtplib.SMTP_SSL('smtp.qq.com')
# 登录邮件箱
smtp.login('dan.ai.ta.ya@qq.com','yxjvgowzsliighbj')
# 发送邮件
smtp.sendmail('dan.ai.ta.ya@qq.com','dan.ai.ta.ya@qq.com',msg.as_string())
# 关闭
smtp.quit()