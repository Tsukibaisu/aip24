#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/4/27 
# Author    : smart
# @File     : send_email_atta.py
# @Software : PyCharm
# 连接邮箱
import smtplib
# 发邮件
from email.mime.text import MIMEText
# 发带附件的邮件
from email.mime.multipart import MIMEMultipart
# 用于使用中文邮件主题
from email.header import Header

with open('report.html',encoding='utf-8') as f:
    email_body=f.read()
# 发送的对象
msg=MIMEMultipart()
# 添加html格式邮件正文（会丢失css格式）
msg.attach(MIMEText(email_body,'html','utf-8'))
# 发件人
msg['From']='dan.ai.ta.ya@qq.com'
# 收件人
msg['To']='dan.ai.ta.ya@qq.com'
# 邮件主题
msg['Subject']=Header('接口测试报告','utf-8')
# 添加附件
att1=MIMEText(
    open('report.html','rb').read(),'base64','utf-8'
)# 二进制打开
att1['Content-Type']='application/octet-stream'
att1['Content-Disposition']='attachment; filename="repost.html'
msg.attach(att1)
# 创建一个stmp的链接
smtp= smtplib.SMTP_SSL('smtp.qq.com')
# 登录邮件箱
smtp.login('dan.ai.ta.ya@qq.com','yxjvgowzsliighbj')
# 发送邮件
smtp.sendmail('dan.ai.ta.ya@qq.com','dan.ai.ta.ya@qq.com',msg.as_string())
# 关闭
smtp.quit()