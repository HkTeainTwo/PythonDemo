#coding=utf-8
import urllib
import re
import math

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html,k):
    reg = r'<img src="(.+?\.jpg)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    x = 0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl,'%s%s.jpg' %(k,x))
        x+=1

for i in range(1, 13):
    i=str(i)
    url="http://www.youmzi.com/meinv_"+i+".html"
    print url
    html = getHtml(url)
    print getImg(html,i)

