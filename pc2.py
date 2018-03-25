# -*- coding:utf-8 -*-
__author__='www.moonsec.com'
import os,sys
import urllib2
import threading
import Queue
q=Queue.Queue()

baidu_spider="Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)"

lines=open("D:\python2.7\example\dir.txt",'r')
for line in lines:
    line=line.rstrip()
    q.put(line)



def scaner():
    while not q.empty():
        path=q.get()
        url="%s%s" % (domain_name,path)
        print path
        headers={}
        headers['User-Agent']=baidu_spider
        requset=urllib2.Request(url,headers=headers)
        try:
            response = urllib2.urlopen(requset)
            content=response.read()
            if len(content):
                print "Status [%s] - path: %s" % (response.code,url)
                wx('sb.txt',url+'\n')
            response.close()
        except urllib2.HTTPError as e:
            pass   
def show():
    print "scandir.py http://www.moonsec.com 10"


def wx(filename,context):
    f= file(filename,"a+")
    f.write(context)
    f.close()


if __name__ == '__main__':
    if len(sys.argv) < 3:
        show()
        sys.exit()
    thread_num=sys.argv[2]
    domain_name=sys.argv[1]
    for i in range(int(sys.argv[2])): 
        t = threading.Thread(target=scaner)
        t.start()


