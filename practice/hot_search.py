import requests
from bs4 import BeautifulSoup
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

url_str="https://search.jd.com/Search?keyword=%E8%B5%9B%E7%9D%BF%E9%94%AE%E7%9B%98&enc=utf-8&spm=2.1.1"
url_s="https://s.weibo.com/top/summary?cate=realtimehot"
resp=requests.get(url=url_s,headers=request_headers)


status_code=resp.status_code
if status_code==200:
    text = resp.text
    soup=BeautifulSoup(text,"html.parser")
    ranks=soup.select('#pl_top_realtimehot > table > tbody > tr:nth-child(1) > td.td-01 > i')
    ranks=ranks+soup.select('#pl_top_realtimehot > table > tbody > tr> td.td-01.ranktop')
    keywords=soup.select('#pl_top_realtimehot > table > tbody > tr > td.td-02 > a')
    peoples=soup.select('#pl_top_realtimehot > table > tbody > tr > td.td-02 ')
    ishots=soup.select('#pl_top_realtimehot > table > tbody >tr> td.td-03 ')

    for rank,keyword,people,ishot in zip(ranks,keywords,peoples,ishots):
        try:
            r=rank.get_text()
        except:
            r=rank.get('class')
        content=keyword.get_text()
        page=keyword.get('href')
        p=' '
        try:
            p=people.find('span').get_text()
        except:
            p=' '
        temp=' '
        try:
            temp=ishot.find('i').get_text()
        except:
            temp=' '
        dic={
            "rank":r,
            "content":content,
            "page":page,
            "click":p,
            "else":temp
        }
        print(dic)