from HTMLParser import HTMLParser
import urllib2

 
class MyHTMLParser(HTMLParser):
    
    def __init__(self):  
        HTMLParser.__init__(self)  
        self.flag=None
        
    def handle_starttag(self, tag, attrs):  
    # �������¶����˴���ʼ��ǩ�ĺ���  
        if tag == 'a':  
    # �жϱ�ǩ<a>������  
            self.flag='a'  
            for name,value in attrs:  
                if name == 'href':  
                    print("href:"+value)  
  
    def handle_data(self,data):  
        if self.flag == 'a':  
            print("data:"+data)  


if __name__ == '__main__':  
    a = '<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd"><html><head><!--insert javaScript here!--><title>test</title><body><a href="http: //www.163.com">���ӵ�163</a></body></html>'  
    my = MyHTMLParser()  
    my.feed(a)
    my.close()
    
