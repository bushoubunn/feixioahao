import requests
from  lxml import etree
import time
from config import header
import re
import json


def get_cooin_info():
    url='https://www.feixiaohao.com/'
    req=requests.Session()
    response=req.get(url,headers=header)
    pattern=r'<div.*?class="new-table.*?new-coin-list".*?<tbody>.*?<tr.*?id=bitcoin(.*?)<tr'
    content=re.search(pattern,response.text,re.X)
    infopattern=r'><td>(.*?)<td>.*?<a.*?<img.*?>(.*?)</a>.*?<td.*?>(.*?)<td>.*?<a.*?>(.*?)</a>.*?<td>(.*?)<td>.*?>(.*?)</a>.*?<span.*?>(.*?)</span>'

    #print(content.groups())

    for texts in content.groups():
        info={}
        infos=re.search(infopattern,texts,re.X)
        #print(infos.groups())
        info['rank']=infos.groups()[0]
        info['name']=infos.groups()[1]
        info['maketcap']=int(infos.groups()[2][1:-1].replace(',',''))
        info['price']=int(infos.groups()[3][1:].replace(',',''))
        info['turnover']=infos.groups()[4]
        info['vol']=infos.groups()[5]
        info['increase']=float(infos.groups()[6][:-1])


    jsons=json.dumps(info,ensure_ascii=False)
    return jsons
#get_cooin_info()