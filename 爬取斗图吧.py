from pyquery import PyQuery as pq
import requests
from redis import StrictRedis
o=0
headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'

}


def xpan(canshu):
    try:
        url = 'https://www.doutula.com/photo/list/?page=' + str(canshu)
        sp = requests.get(url, headers=headers).text

        doc=pq(sp)
        item=doc('.col-xs-6 img').items()

        for i in item:
            cu=i.attr('data-original')



            #r(cu,'F:/斗图的/%s.jpg'%u)
           # u+=1
            #print('当前已保存%d张'%u)
            #print(cu)
            redis = StrictRedis(host='172.18.200.5', port=6379, db=1, password='')
            redis.sadd('斗图网下载图片的URL', cu)

    except Exception as e:

       print('出现错误',e.args)
a=int(input('请问你需要爬取多少页呢:'))
print('正在爬取链接并保存到redis数据库中请稍等........')
for i in range(a):

   xpan(i+1)

redis = StrictRedis(host='172.18.200.5', port=6379, db=1, password='')
redis.srem('斗图网下载图片的URL','None')
for i in redis.smembers('斗图网下载图片的URL'):
    t=str(i,encoding='utf8')
    #print(t)
    r=t.split('/')[-1]
    dizhi='F:/斗图/'+r
    req=requests.get(t)
    with open(dizhi,'wb')as p:
        p.write(req.content)
        print('保存完毕 已保存了%d张'%o)
        o+=1