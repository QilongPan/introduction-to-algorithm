
# -*- coding: utf-8 -*-
# @Date    : 2019-08-15 09:36:08
# @Author  : QilongPan 
# @Email   : 3102377627@qq.com
#coding=utf-8
import smtplib
from email.mime.text import MIMEText
msg_from='xxxxxxxx@qq.com'
#授权码 点击邮件内的设置，账户，然后开启smtp
passwd='dfsdsfasdas'
msg_to='xxxxxxx@qq.com'
                            
subject="python邮件测试"
content="这是我使用python smtplib及email模块发送的邮件"
msg = MIMEText(content)
msg['Subject'] = subject
msg['From'] = msg_from
msg['To'] = msg_to
try:
    s = smtplib.SMTP_SSL("smtp.qq.com",465)
    s.login(msg_from, passwd)
    s.sendmail(msg_from, msg_to, msg.as_string())
    print("发送成功")
except s.SMTPException as e:
    print("发送失败")
finally:
    s.quit()