from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote
from pyquery import PyQuery as pq



broser=webdriver.Chrome()
wait=WebDriverWait(broser,10)
try:
    a=input('请输入你要查找的商品：')
    url='https://list.tmall.com/search_product.htm?q='+quote(a)
    broser.get(url)
    html=broser.page_source
    doc=pq(html)
    items=doc('.product-iWrap').items()
    for i in items:
        #print('i是:',i)
        pro={
            '店铺名':i.find('.productShop-name').text(),
            '成交量':i.find('.productStatus').text(),
            #'图片地址:':i.find('.productImg-wrap img').attr('src'),
            '图片地址':i.attr('src'),
            '内容':i.find('.productTitle a').text(),
            '价格:':i.find('.productPrice').text()
        }
        print(pro)
except TimeoutException:
    print('出错了')
finally:
    broser.close()