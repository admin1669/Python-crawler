'''
1.这个代码是合并 西刺 66 和几个代理网站 并添加用户选择爬取哪个代理网站
2.添加多线程爬取
3.添加多进程爬取
'''

import requests
import re
from threading import Thread
import time
from multiprocessing import Pool


print('*'*30)
print('1.采用普通模式爬取西刺代理(自带检测保存)')
print('2.采用普通模式爬取66代理(自带检测保存)')
print('3.采取多线程模式爬取代理(带检测保存)')
print('4.采取多进程模式爬取代理(带检测保存)')

print('*'*30)





#进行代理IP测试的版块
def test(cansu):
    u=1
    proxy = cansu
    proxies = {
        'http': 'http://' + proxy,
        'https': 'https://' + proxy
        # 'https':'https://'+proxy
    }
    # print(proxies)
    print(proxy)
    try:

        response = requests.get('http://httpbin.org/get', timeout=5, proxies=proxies)
        # print(response.text)
        # print(response.status_code)
        # print('成功%d个' % u, '状态码为:', response.status_code)
        if response.status_code == 200:
            print('成功%d个' % u, '状态码为:', response.status_code)
            er = proxy + '\n'
            with open('可用代理.txt', 'a+')as x:
                x.write(er)
            u += 1
    except Exception as e:
        print('出现错误：', e.args)

headers={
    'User-Agent':'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
}

#爬取西刺代理
def xici(page):
    u=time.time()
    url = 'http://www.xicidaili.com/nn/' + str(page)

    resonp = requests.get(url, headers=headers).text

        # print(resonp)
    repo = re.compile("(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,4}).*?(\d{2,6})", re.S).findall(resonp)

    m = 1
    for li in repo:
         # 如果下面不加\n在写入的时候就是一行写满爬取到的IP和代理 加了 \n就会换行 写入
        # 也可以看出元祖类型可以用下标
        ip = li[0] + ':' + li[1]  # + '\n'
        test(ip)
    print('耗时:',time.time()-u)
#爬取66代理网站
def liuliudaili(page):
    '''

    :param page: 页码数
    :param tar: 这个是爬取哪个代理就传入哪个代理的方法
    :return:
    '''
    for u in range(page):
        url = 'http://www.66ip.cn/' + str(u) + '.html'
        respon = requests.get(url, headers=headers).text
        # print(respon)
        rety = re.compile('(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,4}).*?(\d{1,6})', re.S).findall(respon)
        # test=[]
        u = 1
        for i in rety:
            ip = i[0] + ':' + i[1]  # +'\n'
            # test.append(ip)
            test(ip)

#多线程通用爬取
def dxcty(tar,page):
    '''

    :param page:爬取的页面数
    :return: 线程数
    '''
    tu=time.time()
    ths=[]
    for i in range(page):
        th=Thread(target=tar,args=(i,))
        th.start()
        ths.append(th)
    for u in ths:
        u.join()
    print('耗时:',time.time()-tu)

#多进程通用爬取
def djcty(tar,page):
    el=time.time()
    pool=Pool()
    y=tar
    for i in page:
        pool.apply_async(y,(page,))
    pool.close()
    pool.join()
    print('耗时:',time.time()-el)

iup=input('请输入对应的数字:')
if iup == '1':
    print('此版块是爬取西刺代理 页面最多有3000页+ 但耗时很久 建议5页')
    x=int(input('请输入要爬取的几页:'))
    xici(x+1)

elif iup == '2':
    print('此版块是爬取66代理 页面最多有1000页+ 但耗时很久 建议5页')
    x = int(input('请输入要爬取的几页:'))
    liuliudaili(x+1)

elif iup == '3':
    print('此版块为多线程 需要传入爬取页面数和爬取代理的方法')
    a=int(input('请输入要爬取的页面数:'))
    b=input('请选择方法 1.西刺 2.66')
    if b == '1':

        dxcty(xici,a)
    elif b == '2':
        dxcty(liuliudaili,a)

elif iup == '4':
    print('此版块为多进程 需要传入爬取页面数和爬取代理的方法')
    a = int(input('请输入要爬取的页面数:'))
    b = input('请选择方法 1.西刺 2.66')
    if b == '1':

        dxcty(xici,a)
    elif b == '2':
        dxcty(liuliudaili,a)