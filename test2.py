
# -*- coding: utf-8 -*-
# @Date    : 2019-09-18 18:01:39
# @Author  : QilongPan 
# @Email   : 3102377627@qq.com
from qqbot import _bot as bot
bot.Login(['-q', '3102377627'])
buddy = bot.List('三毛')
# 判断是佛存在这个好友
if buddy:
 b = buddy[0]
 # 发送消息
 bot.SendTo(b, 'nihao')