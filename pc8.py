import urllib2
import urllib
import httplib
import threading





headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:14.0) Gecko/20100101 Firefox/14.0.1'}  
        #构造Post数据，他也是从抓大的包里分析得出的。  
postdata = {
            'username' : 20134964, 
            'password' : 210631, 
            'lt' : '312312',  
           }  
  
#需要给Post数据编码  
postdata = urllib.urlencode(postdata)  
#通过urllib2提供的request方法来向指定Url发送我们构造的数据，并完成登录过程  
request = urllib2.Request("https://matrix.dean.swust.edu.cn/cas/login", postdata, headers)  
#print request  
response = urllib2.urlopen(request)  
text = response.read()
print text
        
