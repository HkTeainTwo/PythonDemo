import urllib2
import urllib
import httplib
import threading





headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:14.0) Gecko/20100101 Firefox/14.0.1'}  
        #����Post���ݣ���Ҳ�Ǵ�ץ��İ�������ó��ġ�  
postdata = {
            'username' : 20134964, 
            'password' : 210631, 
            'lt' : '312312',  
           }  
  
#��Ҫ��Post���ݱ���  
postdata = urllib.urlencode(postdata)  
#ͨ��urllib2�ṩ��request��������ָ��Url�������ǹ�������ݣ�����ɵ�¼����  
request = urllib2.Request("https://matrix.dean.swust.edu.cn/cas/login", postdata, headers)  
#print request  
response = urllib2.urlopen(request)  
text = response.read()
print text
        
