
import urllib.request
request_headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                 'Chrome/91.0.4472.124 Safari/537.36',
    'Connection':'keep-alive'
}

url="http://www.baidu.com"

request=urllib.request.Request(url=url,headers=request_headers)

response=urllib.request.urlopen(request)

#获取并解析处理相应相关信息
status_code=response.getcode()

request_address=response.geturl()
#响应头，响应信息
response_info=response.info()
#获取html源代码
html_test=response.read().decode('utf-8')

print(status_code)
print(request_address)
print(response_info)
print(html_test)