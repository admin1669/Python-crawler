import requests
from pyquery import PyQuery  as pq
i=str(input('请输入歌曲id:'))
url='http://www.kuwo.cn/yinyue/'+i+'?catalog=yueku2016'
response=requests.get(url).text

doc=pq(response)
wrpa=doc('.lrcItem').text()

cu=wrpa.replace(' ','\n')
p=input('是否把歌曲保存到本地 1是 2不要 3直接打印歌词:')
if p == '1':
    u=input('请输入文件名:')
    test=u+'.txt'
    with open(test,'w')as p:
        p.write(cu)
        print('保存完毕请到本地查看')
elif p=='3':
    print(cu)
else:
    print('退出')



