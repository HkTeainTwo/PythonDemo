# -*- coding: utf-8 -*-
import urllib2
import ssl
import cookielib
from  HTMLParser import HTMLParser 

class MyHTMLParser(HTMLParser):
    
    def __init__(self):  
        HTMLParser.__init__(self)  
        self.flag=None
        
    def handle_starttag(self, tag, attrs):  
    # 这里重新定义了处理开始标签的函数  
        if tag == 'td':  
    # 判断标签<a>的属性  
            self.flag='a'  
            for name,value in attrs:  
                if name == 'href':  
                    print("href:"+value)  
  
    def handle_data(self,data):  
        if self.flag == 'a':  
            print("data:"+data)  
 
    

ssl._create_default_https_context = ssl._create_unverified_context
headers={'Cookie':'SSO=TGC%2Ddb411e7c40857b7a7d655f2efee1aa19c14dc4b9d42b173c11d07dc3de40920f6b771ceade659bd2aed84428b0cb660ee544c64530936c55bbc85102f796cd79fda1bd638a37600d8608d7abeb5ba922e2944e7f193ce04aee4f3a7c74c607428eaaf417c38bb51272df6414e4382c454d727cde1d95ce3c3b183521856f54a0c7c01602e998dfbb38472b21972f088a972a16de54d60e16dd63921e77825ddc053ef81d325aa17333d99dcd8762e17e164cfde7d1c848c4004b8b4c90ffdc9af3cd2d59a9bae5ecca0eaba74f819cb3a9ea593365457c5547333a419a8275b2685a1cb17192da8cdd3344463a7e56a84640218bb18862d8','User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:47.0) Gecko/20100101 Firefox/47.0','Referer':'https://matrix.dean.swust.edu.cn/acadmicManager/index.cfm?event=studentProfile:courseMark','Connection':'keep-alive','Host':'matrix.dean.swust.edu.cn'}
req=urllib2.Request('https://matrix.dean.swust.edu.cn/acadmicManager/index.cfm?event=studentProfile:courseMark',headers=headers)
r=urllib2.urlopen(req)
rr=r.read()
print rr
m = MyHTMLParser()  
m.feed(rr)
m.close()
#cookie=cookielib.CookieJar()
#opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
#response=opener.open('https://matrix.dean.swust.edu.cn/acadmicManager/index.cfm?event=studentPortal:DEFAULT_EVENT&ticket=ST-DCC78046-F86A-7D78-2C70763AE344231A')
#text = response.read()
#print text
##    #for i in cookie:
#   print i
