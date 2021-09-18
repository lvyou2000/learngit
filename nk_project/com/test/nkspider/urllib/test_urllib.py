import urllib.request
import os

# 获取图片
# 获取地址解析
url = "https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png"
# 发送url请求，获得响应
resp = urllib.request.urlopen(url)
# 获取相应内容
resp_content = resp.read()
# 获取实际数据
data = resp_content

file_name = "baidu.png"
# file_name=url.split("/")[-1]
# 获取当前文件夹所在文件夹下的data目录
file_path = os.path.join(os.getcwd(), 'data')

with open(file_path + os.sep + file_name, 'wb') as fp:
    fp.write(data)
    print("End....")
