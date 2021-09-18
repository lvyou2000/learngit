import csv
import json
import requests
from bs4 import BeautifulSoup
import time
import random

user_agents = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
]

# 随机获取 user-agent, 实现 反 反爬 操作
request_headers = {
    'User-Agent': random.choice(user_agents)
}

ips=['220.184.35.129', '59.55.166.77', '223.241.78.13', '60.5.172.211', '61.161.29.244', '49.81.233.169',
     '221.122.91.60', '223.240.209.121', '59.55.162.214', '61.161.28.230', '61.161.30.192',
     '182.139.110.41', '183.147.222.48', '171.13.84.216', '61.154.64.76', '60.7.209.83', '118.117.188.173', '27.191.60.142',
     '112.195.240.253', '182.84.145.168', '60.7.209.83', '118.117.188.173', '27.191.60.142', '112.195.240.253',
     '182.84.145.168', '171.44.192.13', '61.161.27.48', '223.241.118.92', '223.244.179.164', '61.131.45.230', '175.7.199.120',
     '60.31.89.11', '223.244.179.32', '27.159.165.188', '60.182.190.205', '59.55.162.7', '182.84.145.213', '106.45.104.124',
     '61.161.29.241', '221.122.91.75', '59.55.162.7', '182.84.145.213', '106.45.104.124', '61.161.29.241', '221.122.91.75',
     '36.57.89.69', '223.214.219.204', '223.240.208.72', '27.159.167.161', '59.55.166.136', '183.166.87.92', '182.84.144.61',
     '47.101.41.26', '58.255.206.53', '59.55.162.164', '220.184.32.245', '27.159.165.217', '202.109.157.62', '59.55.162.138',
     '27.159.167.204', '220.184.32.245', '27.159.165.217', '202.109.157.62', '59.55.162.138', '27.159.167.204', '59.55.161.140',
     '60.31.89.178', '219.159.38.199', '222.74.65.83', '182.105.200.84', '223.240.209.235', '61.161.27.127', '27.191.60.190',
     '60.168.206.93', '117.69.230.184', '60.168.206.19', '60.182.188.226', '223.244.179.79', '183.165.128.128', '49.85.15.144',
     '60.168.206.19', '60.182.188.226', '223.244.179.79', '183.165.128.128', '49.85.15.144', '61.131.45.236', '60.7.208.110',
     '183.166.125.87', '60.7.28.45', '60.7.210.83', '59.54.20.150', '59.55.166.148', '61.161.28.185', '49.89.86.112', '60.7.31.189',
     '58.220.95.44', '223.242.246.176', '183.166.86.215', '60.168.206.120', '60.168.80.150', '58.220.95.44', '223.242.246.176',
     '183.166.86.215', '60.168.206.120', '60.168.80.150', '61.161.29.19', '60.7.100.103', '27.191.60.64', '220.179.210.22',
     '124.192.87.89', '60.31.89.135', '27.205.40.181', '60.7.98.56', '60.7.29.46', '49.86.9.48', '59.55.162.61', '61.154.64.45',
     '27.192.168.127', '182.84.145.35', '59.55.162.186', '59.55.162.61', '61.154.64.45', '27.192.168.127', '182.84.145.35',
     '59.55.162.186', '60.31.89.73', '60.168.80.201', '182.105.200.45', '61.191.85.75', '223.240.208.35', '47.100.207.132',
     '61.154.64.161', '27.159.166.55', '60.7.31.98', '59.55.162.40', '61.161.27.65', '60.7.209.18', '27.191.60.145', '60.7.29.86',
     '183.158.65.168', '61.161.27.65', '60.7.209.18', '27.191.60.145', '60.7.29.86', '183.158.65.168', '27.191.60.61',
     '59.55.161.179', '27.191.60.30', '61.161.29.234', '61.161.27.254', '61.161.29.216', '60.167.82.6', '27.159.164.11',
     '47.92.158.181', '60.7.97.118', '59.55.164.133', '223.214.219.21', '47.94.100.76', '60.5.172.77', '60.5.173.120',
     '59.55.164.133', '223.214.219.21', '47.94.100.76', '60.5.172.77', '60.5.173.120', '27.191.60.240', '60.205.132.71',
     '59.55.166.11', '59.55.162.174', '183.166.87.230', '61.161.28.109', '60.7.102.54', '59.55.160.110', '223.214.219.133',
     '61.161.27.168', '61.191.85.90', '60.167.22.75', '175.7.199.36', '60.173.46.214', '182.87.138.97']


x1=0
k=1
m=0
proxies={'https':ips[m]}
# for i in range(0,186,30):
#     url_ss="https://search.jd.com/Search?keyword=%E5%8D%8E%E4%B8%BA%E8%8D%A3%E8%80%8050&qrst=1&suggest=1.def.0.base" \
#            "&wq=%E5%8D%8E%E4%B8%BA%E8%8D%A3%E8%80%8050&ev=exbrand_%E8%8D%A3%E8%80%80%EF%BC%88HONOR%EF%BC%89%5E&pvid=d7a78c24" \
#            "df6a466689b5ecc31a8a87a0&page={0}&s={1}&click=0".format(x1,i)
#     x1=x1+1
url_ss="https://search.jd.com/Search?keyword=%E9%94%AE%E7%9B%98%E6%9C%BA%E6%A2%B0&enc=utf-8&suggest=1.def.0.base" \
       "&wq=%E9%94%AE%E7%9B%98&pvid=a3ea0ee648874e91869631a721813552";
resp=requests.get(url=url_ss,headers=request_headers)
if resp.status_code==200:
    web_text=resp.text  
    soup=BeautifulSoup(web_text,"html.parser")
    nums=soup.select('#J_goodsList > ul > li')
    for num in nums:
        n=num.get('data-sku')
        print(n)
        for i in range(100):
            url_str="https://club.jd.com/comment/productPageComments.action?productId={0}&score=0&sortType=5&page={1}&pageSize=10".format(n,i)
            i=i+1
            try:
                resp2 = requests.get(url=url_str, headers=request_headers)
                if resp2.status_code == 200:
                    print("------------------------" + str(k) + "------------------------")
                    k = k + 1

                    resp_json_str = resp2.content.decode("gb18030")
                    resp_json_data=json.loads(resp_json_str)
            except:
                m=m+1
                i=i-1
                continue
            comments=resp_json_data["comments"]
            hotCommentTagStatistics=resp_json_data["hotCommentTagStatistics"]
            if len(comments)==0:
                print("无评论")
                break

            for comment in comments:
                content=comment["content"].strip()
                score=comment["score"]
                print(content+"   score:"+str(score))
                row=[content,score]
                out = open("jd_all_comments.csv", "a", newline="", encoding="utf-8")
                csv_writer = csv.writer(out)
                csv_writer.writerow(row)
                if score==5:
                    row2 = [content]
                    out2 = open("jd_good_comments.csv", "a", newline="", encoding="utf-8")
                    csv_writer = csv.writer(out2)
                    csv_writer.writerow(row2)
            time.sleep(random.uniform(2.1, 5.5))

