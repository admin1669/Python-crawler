from pyquery import PyQuery as pq
import requests
import urllib.parse as p
#自己写入微博的URL 这个是Ajax接口Url
base_url='https://m.weibo.cn/api/container/getIndex?'
headers={
    '改成自己的User-Agent',
    'X-Requested-With':'XMLHttpRequest'

}

def get(page):
    params={
        'type': 'uid',
        'value': '2830678474',
        'containerid': '1076032830678474',
        'page': page
    }
    url=base_url+p.urlencode(params)
    try:
        response=requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print('error:',e)

def parse_set(json):
    if json:
        items=json.get('data').get('cards')
        print('此时的items是啥:',items)
        for i in items:
            item=i.get('mblog')
            weibo={}
            #还可添加别的条目
            weibo['id']=item.get('id')
            weibo['正文']=pq(item.get('text')).text()
            weibo['点赞数目']=item.get('attitudes_count')
            weibo['评论数']=item.get('comments_count')
            weibo['转发数:']=item.get('reposts_count')
            #生成器
            yield weibo

if __name__=='__main__':
    for page in range(2,11):
        json=get(page)
        test=parse_set(json)
        for t in test:
            print(t)
