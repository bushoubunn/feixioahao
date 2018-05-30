import requests
from  lxml import etree
import time
from config import header
import re
import json

url='https://www.feixiaohao.com/'
req=requests.Session()
response=req.get(url,headers=header)
pattern=r'<div.*?class="new-table.*?new-coin-list".*?<tbody>.*?<tr(.*?)<tr(.*?)<tr(.*?)<tr'
content=re.search(pattern,response.text,re.X)
infopattern=r'id.*?<td>(.*?)<td>.*?<a.*?<img.*?>(.*?)</a>.*?<td.*?>(.*?)<td>.*?<a.*?>(.*?)</a>.*?<td>(.*?)<td>.*?>(.*?)</a>.*?<span.*?>(.*?)</span>'

infolist=[]
#print(content.groups())

for texts in content.groups():
    info={}
    infos=re.search(infopattern,texts,re.X)
    #print(infos.groups()[10])
    info['rank']=infos.groups()[0]
    info['name']=infos.groups()[1]
    info['maketcap']=infos.groups()[2]
    info['price']=infos.groups()[3]
    info['turnover']=infos.groups()[4]
    info['vol']=infos.groups()[5]
    info['increase']=infos.groups()[6]
    infolist.append(info)

json=json.dumps(infolist,ensure_ascii=False)
print(json)
