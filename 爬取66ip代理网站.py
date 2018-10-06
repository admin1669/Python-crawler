import re
import requests
#url='http://www.66ip.cn/9.html'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
}


def page_get(page):

    url = 'http://www.66ip.cn/'+str(page)+'.html'''
    respon = requests.get(url, headers=headers).text
    #print(respon)
    rety=re.compile('(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,4}).*?(\d{1,6})',re.S).findall(respon)
    #test=[]
    u=1
    for i in rety:
        ip=i[0]+':' + i[1] #+'\n'
        #test.append(ip)

        proxy=ip
        proxies={
            'http':'http://'+proxy,
            'https':'https://'+proxy
            #'https':'https://'+proxy
        }
        #print(proxies)
        print(proxy)
        try:

            response = requests.get('http://httpbin.org/get', timeout=5, proxies=proxies)
            # print(response.text)
            # print(response.status_code)
            #print('成功%d个' % u, '状态码为:', response.status_code)
            if response.status_code == 200:
                print('成功%d个' % u, '状态码为:', response.status_code)
                er = proxy + '\n'
                with open('66代理网IP.txt', 'a+')as x:
                    x.write(er)
                u += 1
        except Exception as e:
            print('出现错误：',e.args)

print(page_get(1))