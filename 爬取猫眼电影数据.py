import requests

from pyquery import PyQuery as pq
url='https://box.maoyan.com/promovie/api/box/second.json'
headers={

    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
}
response=requests.get(url,headers=headers)
if response.status_code==200:
    test=response.json()

else:
    print('不是200')

if test:

    items=test.get('data').get('list')
    #print(items)
    for item in items:
        #print(items)
        shuju={}
        shuju['片名']=item.get('movieName')
        shuju['上映天数']=item.get('releaseInfo')
        shuju['综合票房']=item.get('boxInfo')
        shuju['收入票房']=item.get('sumBoxInfo')
        shuju['票房占比']=item.get('showRate')
        shuju['上座率']=item.get('avgSeatView')
        shuju['场均人次']=item.get('avgShowView')

        print(shuju)
