import requests
from pyquery import PyQuery as pq
import re

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
}

#Url='https://www.qu.la/book/161/131487.html'


#进入小说文章中爬取内容
def content(Url):
    sponse=requests.get(Url,headers=headers).text
    doc=pq(sponse)
    text=doc('#content').text()
    return text


#抓取URL
def Grab_the_URL():

    print('像https://www.qu.la/book/41946/这个 book后面41946就是书名号')
    inputurl=input('请输入书名号:')
    io = 1
    url='https://www.qu.la/book/%s/'%inputurl
    sponse=requests.get(url,headers=headers).text
    doc=pq(sponse)
    URL=doc('#list a').items()
    for i in URL:
        #print(i.attr('href'))
        RE=re.compile('(/book/.*?.html)',re.S).findall(i.attr('href'))
        for r in RE:

            #小说内容的URL
            text='https://www.qu.la/'+r
            The_request_again=requests.get(url=text,headers=headers).text
            doc = pq(The_request_again)
            The_novel_title = doc('.bookname').items()
            for u in The_novel_title:

                Stitle=u.find('h1').text()
                c=content(text)

                #print(c)

                with open('F:/小说/第%s章.txt'%io,'w',encoding="utf-8")as p:
                    p.write(c)
                    print('当前已爬取%s章节了 请您耐心等待'%io)


            io+=1

Grab_the_URL()

