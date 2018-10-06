import requests
from selenium import webdriver
from pyquery import PyQuery as pq
import pymongo
from bs4 import BeautifulSoup

clien=pymongo.MongoClient(host='改成自己的数据库IP')
db=clien.Used_car
coll=db.The_car

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
}
def A_used_car(page):
    Url='https://www.guazi.com/gl/buy/o%s/#bread'%page
    brow=webdriver.Chrome()
    brow.get(Url)
    Web_content=brow.page_source
    doc=pq(Web_content)
    content=doc('.car-a').items()
    for i in content:
        #cute=pq(i.find('.t').html()).text()
        #print(cute)
        #print(i.find('.car-a').attr('title'))
        data={
            '车名字':i.attr('title'),
            '年数和里程数':i.find('.t-i').text().replace('\n',''),
            '价格':i.find('.line-through').text()
        }
        print(data)
        coll.insert_one(data)
    brow.close()

for i in range(1,65):
    A_used_car(i)