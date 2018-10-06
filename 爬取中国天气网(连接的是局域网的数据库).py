import requests
from pyquery import PyQuery as pq
import pymongo


#爬取一个星期的天气
def cute():
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
    }
    url='http://www.weather.com.cn/weather/101300501.shtml'
    sponse=requests.get(url,headers=headers)
    sponse.encoding='utf8'
    c=sponse.text
    doc=pq(c)
    riqi=doc('.sky.skyid').text()
    print(riqi)


#获取8-15天的天气
def weather():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
    }
    url='http://www.weather.com.cn/weather15d/101300501.shtml'
    sponse=requests.get(url,headers=headers)
    sponse.encoding = 'utf8'
    c = sponse.text
    doc=pq(c)
    bashiwu=doc('.t').text()
    print(bashiwu)

def yanzheng():
    name = input('请输入用户名：')
    passwd = input('请输入密码:')
    res = coll.find_one({'用户名': name})
    if (name == res['用户名']) and (passwd == res['密码']):
        print('*'*30)
        print('账号密码正确可以使用此软件的功能')
        print('*'*30)

clien=pymongo.MongoClient(host='172.18.200.5')
db=clien.namepasswd
coll=db.np


print('*'*30)
print('0.注册账户')
print('1.查询这个星期的7天的天气')
print('2.查询8天后-15天的天气')
print('输入其他键退出软件')
print('*'*30)

while True:
    ii=input('请输入对应的数字:')

    if ii=='0':
        a=input('请输入用户名:')
        b=input('请输入密码:')
        test={
            '用户名':a,
            '密码':b
        }
        coll.insert(test)

    elif ii=='1':
        yanzheng()
        cute()

    elif ii=='2':
        yanzheng()
        weather()

    else:
        print('账号和密码错误或者你选择退出的')
        break