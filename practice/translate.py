import urllib.request
import urllib.parse
import json
import time  #如果需要模拟人的话，加上时间限制，每过几秒访问一次，防止服务器进行限制

#while true
#如果输入某个特定的的值的话才可以退出，否则持续循环
content=input("请输入需要翻译的：")
url='http://fanyi.youdao.com/translate'
data = {}
data['i']= content
data['from']= 'AUTO'
data['to']='AUTO'
data['smartresult']= 'dict'
data['client']=' fanyideskweb'
data['salt']= '16145146187866'
data['sign']= 'dfb549818743ca5255276e33da4669bd'
data['lts']= '1614514618786'
data['bv']= '51c157d16589f89e7109f585b4553d23'
data['doctype']= 'json'
data['version']= '2.1'
data['keyfrom']= 'fanyi.web'
data['action']='FY_BY_CLICKBUTTION'

data=urllib.parse.urlencode(data).encode('utf-8')
response=urllib.request.urlopen(url,data)
html=response.read().decode('utf-8')
target=json.loads(html)
print("翻译的结果：%s"%(target['translateResult'][0][0]['tgt']))
#time.sleep(5) 睡5秒