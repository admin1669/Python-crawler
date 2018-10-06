import requests
from pyquery import PyQuery as pq
import json
#import requests.exceptions as w
from requests.exceptions import ConnectionError,ChunkedEncodingError as w
import re
from threading import Thread
import time

t=time.time()

headers={
    'User-Agent':'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
}
def get_page(page):

    url = 'http://www.xicidaili.com/nn/'+page

    resonp=requests.get(url,headers=headers).text
   # print(resonp)
    repo=re.compile("(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,4}).*?(\d{2,6})",re.S).findall(resonp)
    test=[]
    m=1
    for li in repo:

       #如果下面不加\n在写入的时候就是一行写满爬取到的IP和代理 加了 \n就会换行 写入
       #也可以看出元祖类型可以用下标
        ip = li[0] +':'+ li[1] #+ '\n'
        print(ip)
        #开始测试可用的代理

        proxy=ip
        proxies={
            'http':'http://'+proxy,
            'https':'https://'+proxy
        }
        print(proxies)
        try:

            response=requests.get('http://httpbin.org/get',timeout=15,proxies=proxies)
            #print(response.text)
            #print(response.status_code)
            print('成功%d个'%m,'状态码为:',response.status_code)
            if response.status_code == 200:
                er=proxy+'\n'
                with open('代理IP.txt','a+')as x:
                    x.write(er)
            m+=1
        except Exception as e:
            print('Error',e.args)


    # with open('代理ip.txt','a')as o:
    #            # o.write(ip)
    #
    #     #print(resonp)
    #     #doc=pq(resonp)
    #     #items=doc('.odd').items()
    #     #for i in items:
    #         #oppo={}
    #        # oppo['ip 端口 服务器地址 是否匿名 类型 存活天数 验证日期']=i.text()
    #         #print(oppo)
    #         #with open('代理IP.txt','a+')as c:
    #            # c.writelines(json.dumps(oppo))


#爬取时网页有3300多页 所以循环里的次数可自行更改
#爬取3000多页可用代理 请用服务器所以VPS这些7*24小时的 不然爬取一半关掉 下次还得重来

#添加多线程来给程序爬取速度提提速
#class modopo(threading.Thread):
#    def __init__(self):
 #       threading.Thread.__init__(self)
  #  def run(self):

#sta=modopo()
#sta.start()
#sta.join()
print('执行完毕')
for p in range(2):
    print('此时的p是:', p)
    th=Thread(target=get_page(str(p)))
    th.start()
print(time.time() - t)