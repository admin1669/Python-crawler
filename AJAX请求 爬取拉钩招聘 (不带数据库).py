import requests
import urllib.parse as p
headers={
    'Host':'www.lagou.com',
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Mobile Safari/537.36',
    'X-Anit-Forge-Code':'0',
    'X-Anit-Forge-Token':'None',
    'X-Requested-With':'XMLHttpRequest',
    'Cookie':'user_trace_token=20180717152050-eef2d5c9-8991-11e8-9c4c-525400f775ce; LGUID=20180717152050-eef2d9f4-8991-11e8-9c4c-525400f775ce; index_location_city=%E5%85%A8%E5%9B%BD; JSESSIONID=ABAAABAACBHABBI62D3886D1AC5FE929AC32638B85A34F8; _gat=1; PRE_UTM=; PRE_HOST=www.sogou.com; PRE_SITE=https%3A%2F%2Fwww.sogou.com%2Flink%3Furl%3DhedJjaC291NlQquFD-D9iO8HqdeMO9Y0; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; TG-TRACK-CODE=index_search; _ga=GA1.2.2120420620.1531812049; LGSID=20180717164521-bd358845-899d-11e8-9e0d-5254005c3644; LGRID=20180717164532-c4050f5b-899d-11e8-9e0d-5254005c3644; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1531812049,1531817120; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1531817131; SEARCH_ID=1fdac3b38ab44007a94e9ec3d8fcecea',
    'Referer':'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
}
data={
    'first':'true',
    'pn':'1',
    'kd':'python'
}
test=p.urlencode(data)
#pn是页码 kd是职位
def get_url(pn,kd):
    data = {
        'first': 'true',
        'pn': pn,
        'kd': kd
    }
    #https://www.lagou.com/jobs/companyAjax.json?px=default&city=%E4%B8%8A%E6%B5%B7&needAddtionalResult=false
    #上面这个URL无法爬取 只能爬取下面这个
    url='https://www.lagou.com/jobs/positionAjax.json?px=default&city=%E4%B8%8A%E6%B5%B7&needAddtionalResult=false'
    try:
        response=requests.post(url,headers=headers,data=data)
        # result=resp.json()['content']['positionResult']['result']
        result = response.json()['content']['positionResult']['result']

        for i in result:
            positionName = []

            positionName.append('职位:'+i['positionName' ]+' '+'要求最低学历:'+i['education']+' '+'公司名字:'+i['companyShortName']+' '+'工资：'+i['salary']+' '+'工作类型::'+i['firstType']+' '+'待遇：'+i['positionAdvantage'])
            print(positionName)

'''
def parse_opo(json):
    if json:
        items=json.get('content').get('positionResult')
        print(items)

        for item in items:
            item=item.get('result')
            shuju={}
            shuju['地点']=item.get('city')
            shuju['最低学历']=item.get('education')
            shuju['公司名字']=item.get('companyFullName')
            shuju['招聘人数']=item.get('companySize')
            shuju['工资']=item.get('salary')
            #yield  shuju

'''
a=input('请输入页码:')
b=input('请输入职位:')
get_url(a,b)