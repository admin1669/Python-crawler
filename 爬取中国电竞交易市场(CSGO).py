import requests
from pyquery import PyQuery as pq
import pymongo

clien=pymongo.MongoClient(host='自己的数据库地址')
db=clien.c5
coll=db.information
top={}
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
}
def sp(page):
    page_url='https://www.igxe.cn/csgo/730?is_buying=0&is_stattrak%5B%5D=0&is_stattrak%5B%5D=0&sort=0&ctg_id=0&type_id=0&page_no='+str(page)

    sponse=requests.get(page_url,headers=headers).text
    doc=pq(sponse)
    items=doc('.dataList .single').items()
    for i in items:
        pro={
            '枪名':i.find('.name').text(),
            '枪的图片':i.find('.img img').attr('src'),
            '在售数量':i.find('.c-2').text(),
            '售价':i.find('.c-4').text()
        }
        coll.insert_one(pro)

        print(pro)

for i in range(1,377):
    sp(i)