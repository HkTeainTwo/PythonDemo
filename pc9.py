#  -*- coding: utf-8 -*-
# !/usr/bin/python

import urllib2
import urllib
import cookielib
import re
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
auth_url = 'https://matrix.dean.swust.edu.cn/cas/login'
home_url = 'https://matrix.dean.swust.edu.cn/cas/login';
# 登陆用户名和密码
data={
	"username":"20134964",
	"password":"210631"
}
# urllib进行编码
post_data=urllib.urlencode(data)
# 发送头信息
headers ={
	"Host":"https://matrix.dean.swust.edu.cn", 
	"Referer": "https://matrix.dean.swust.edu.cn"
}
# 初始化一个CookieJar来处理Cookie
cookieJar=cookielib.CookieJar()
# 实例化一个全局opener
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJar))
# 获取cookie

req=urllib2.Request(auth_url,post_data,headers)
result = opener.open(req)
# 访问主页 自动带着cookie信息
result = opener.open(home_url)
# 显示结果
print result.read()
