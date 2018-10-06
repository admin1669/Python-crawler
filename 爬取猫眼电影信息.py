from selenium import webdriver
import requests
from pyquery import PyQuery as pq
from urllib.parse import quote
#由于猫眼官方是不是ajax请求
werser=webdriver.Chrome()


def get_index():
    try:
        a = input('请输入电影的编号:')
        url='http://maoyan.com/films/'+quote(a)
        #print(url)
        werser.get(url)
        html=werser.page_source
        #print(html)
        doc=pq(html)
        items=doc('.dra').text()
        print('剧情简介：'+items)
        print('下面输出用户对此电影的评论')
        item=doc('.user .name').text()
        ite=doc('.comment-content').text()
        print(item + '用户：' + ite,'\n')


        print('图集地址')
        it=doc('.tab-img .clearfix .default-img').items()

        for i in it:
            #print(i)
            print('地址:',i.attr('data-src'))

    except Exception as e:
        print('Errer:',e)
    finally:
        werser.close()

get_index()