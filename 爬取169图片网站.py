import requests
from pyquery import PyQuery as pq
import os
headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
}

#下载图片的模块
def Download_the_module(file,tehurl):
    count = 1
    # 进入网站下载图片
    The_second_request = requests.get(tehurl, headers=headers).text
    # 下载
    The_doc = pq(The_second_request)
    Download_the_pictures = The_doc('.big_img')
    Take_out_the=pq(Download_the_pictures.html())
    Extract_the=Take_out_the.find('img').items()
    for i in Extract_the:
        save=i.attr('src')
        #print(save)
        The_sponse=requests.get(save,headers=headers)
        The_name='F:/图片/'+file
        Save_the_address = str(The_name)
        # 检测是否有image目录没有则创建
        if not os.path.exists(Save_the_address):


            os.makedirs('F:/图片/' + file)
        else:


            with open(Save_the_address+'/%s.jpg'%count,'wb')as f:
                f.write(The_sponse.content)
                print('已经下载了%s张'%count)
            count += 1
#爬取地址
def Climb_to_address(page):

    URL='https://www.169tp.com/gaogensiwa/list_3_%s.html'%page
    sponse=requests.get(URL,headers=headers)
    sponse.encoding='gbk'
    encodin=sponse.text
    doc=pq(encodin)
    extract=doc('.pic').items()
    for i in extract:
        #文件名
        The_file_name=i.text()
        #提取到的网站
        The_url=i.attr('href')

        Download_the_module(The_file_name,The_url)

#一共有616页
a=int(input('请输入开始爬取的页数:'))
b=int(input('请输入结束爬取的页数:'))
Climb_to_address(a,b)