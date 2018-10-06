import requests
from pyquery import PyQuery as pq
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
}


def qiotiantinaqi():
    url='http://tianqi.sogou.com/mutil?town_py=guilin&showDay=7'
    sponse=requests.get(url,headers=headers).text
    doc = pq(sponse)
    ttest = doc('.p1').text()
    opo = ttest.split(' ')
    for i in opo:
        print(i)

def shiwutian():
    url='http://tianqi.sogou.com/mutil?town_py=guilin'
    sponse=requests.get(url,headers=headers).text
    doc = pq(sponse)
    ttest = doc('.p1').text()
    opo = ttest.split(' ')
    for i in opo:
        print(i)

print('*'*50)
print('         欢迎使用天气查询系统')
print('         此系统现只支持广西桂林市区')
print('         后续更新会有更多城市')
print('*'*50)
print('1.查询7天内的天气 2.查询15天内的天气')
a=input('请输入对应的数字:')

if a == '1':
    qiotiantinaqi()

elif a == '2':

    shiwutian()