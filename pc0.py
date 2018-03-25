#coding=utf-8
import urllib
import re
import math

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html


url='http://127.0.0.1/pc.php'
print   getHtml(url)

