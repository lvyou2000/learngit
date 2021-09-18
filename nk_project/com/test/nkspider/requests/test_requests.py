import requests

request_headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                 'Chrome/91.0.4472.124 Safari/537.36',
    'Connection':'keep-alive'
}

url_str="http://www.nankai.edu.cn"

resp=requests.get(url=url_str,headers=request_headers)

# status_code=resp.status_code

# if status_code==200 :
if resp.status_code==200:
    print("success")
    try:
        # html_text=resp.text # 获取页面的源代码
        print(resp.text)
    except ConnectionError:
        print("connection error")

else:
    print("false")