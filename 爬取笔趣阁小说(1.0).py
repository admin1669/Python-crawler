import requests
from pyquery import PyQuery as pq
import re
print('*'*40)
print('*此程序针对笔趣阁小说网站设计的             ')
print('*网站的URL：https://www.qu.la/             ')
print('*此程序为1.0版本 代码写的很烂 后期优化代码和速度')
print('*'*40)
url='https://www.qu.la/book/3775/'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
}
html_info=requests.get(url=url,headers=headers).text
#print(html_info)
doc=pq(html_info)
items=doc('.box_con #list').items()
test=[]
#print(html_info)
io=0
for i in items:
    a=doc('a').items()
    for u in a:
        uy=u.attr('href')
        p=re.compile('/book/3775/.*?\.html',re.S).findall(uy)

        for u in p:
            b='https://www.qu.la/book/'+u
            #print(b)


            cu=requests.get(url=b).text
            #print(cu)
            doc=pq(cu)
            #获取小说章节
            #it=doc('.bookname h1')
            #获取小说内容
            ite=doc('#content')
            #c=it.text()
            #tu=c+'.txt'

            d=ite.text()
            #print(tu)

            with open('F:/小说/第%s章.txt'%io,'w')as p:

                p.write(d)
                print('当前已爬取%s章节了 请您耐心等待'%io)
            io+=1




