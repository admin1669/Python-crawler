import requests
from redis import StrictRedis
url='http://www.mzitu.com/'
redis=StrictRedis(host='172.18.200.5', port=6379, db=0, password='')
#c=redis.smembers('可用代理')
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
}
for i in redis.smembers('可用代理'):
    t=str(i,encoding='utf8')
    test=t .replace('\n','')
    proxies={
        'http':'http://%s'%test
    }
    response=requests.get('http://www.baidu.com/',headers=headers,proxies=proxies)
    o=1
    if response.status_code == 200:
        redis.sadd('成功代理',test)
        print('当前代理可以使用 ip为:',test,'当前成功为%d'%o,'个')
    else:
        redis.sadd('失效代理ip',test)
        print('失效一个')

