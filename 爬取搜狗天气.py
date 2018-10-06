import requests
from pyquery import PyQuery as pq
import pymongo
import time

#连接数据库
clien=pymongo.MongoClient(host='设置为自己的mongodbIP',port=27017)
#指定数据库
db=clien.tianqi
#指定集合
coll=db.tianqibianhua

def spon():
    url='http://tianqi.sogou.com/?tid=101300501'
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
    }
    sponse=requests.get(url,headers=headers).text

    doc=pq(sponse)
    test=doc('.num').text()
    shidu=doc('.hundity').text()
    kongqi=doc('.liv-text').text()
    shijian=doc('.row2.row2-0 .date').text()
    hourweather=doc('.hours-list .list-item')
    cupo='24小时温度变化情况:'+hourweather.text()
    opp=str(cupo)
    ttest=opp.replace('\n',' ')
    #print(ttest)
    tianiqi={
        '时间:':time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) ,
        '当前温度为':test,
        '空气质量':kongqi,
        '湿度':shidu
    }
    coll.insert(tianiqi)




while True:
    spon()
    time.sleep(3600)