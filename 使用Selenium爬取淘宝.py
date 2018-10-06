from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote
from pyquery import PyQuery as pq
browser=webdriver.Chrome()
wait=WebDriverWait(browser,10)
a=input('请输入你想要查找的商品:')
KEYWORD=a
def index_page(page):
    print('当前爬取%s页'%page)
    try:

        url='https://s.taobao.com/search?q='+quote(KEYWORD)
        #print(url)
        browser.get(url)
        if page>1:
            input=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form > input')))
            #submit=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager div.form > span.btn.J_Submit')))
            #EC.presence_of_element_located
            submit = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager div.form > span.btn.J_Submit')))
            input.clear()
            input.send_keys(page)
            submit.click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active > span'), str(page)))
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.m-itemlist .items .item')))
        get_products()
    except TimeoutException:
        index_page(page)
def get_products():
    html=browser.page_source
    #print(html)
    doc=pq(html)

    items = doc('#mainsrp-itemlist .items .item').items()
    #print(1)
    for item in items:

        #print(item)

        for item in items:
            product = {
                '图片地址': item.find('.pic .J_ItemPic').attr('data-src'),
                '价格': item.find('.price').text(),
                '多少人付款': item.find('.deal-cnt').text(),
                '内容': item.find('.title').text(),
                '店铺名': item.find('.shop').text(),
                '地点': item.find('.location').text()
            }
            print(product)
MAX_PAGE=100
for u in range(1,101):
    index_page(u)
'''
        product={
            'image':item.find('.pic .J_ItemPic.img').attr('data-src'),
            'price':item.find('.price').text(),
            'deal':item.find('.deal-cnt').text(),
            #'title':item.find('#J_Itemlist_TLink_566940629944 span.baoyou-intitle.icon-service-free').text(),
            'shop':item.find('shop').text(),
            'location':item.find('.location').text()
        }
        '''