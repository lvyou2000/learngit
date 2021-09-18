import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_new_urls(page_url):
    _urls=[]
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.81"}
    res=requests.get(page_url,headers=head)
    if res.status_code !=200:
        print('failed! : '+ page_url)
        return  None
    res_content=res.json().get('cards')
    if res_content:
        for item in res_content:
            _urls.append('http:'+item['scheme'])
        return _urls
    else:
        print('parse failed!:'+page_url)
        return None


def get_one_news(news_url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.81"}
    res=requests.get(news_url,headers=head)
    if res.status_code!=200:
        print('failed:'+news_url)
        return None
    res.encoding='utf-8'
    # try:
    soup=BeautifulSoup(res.text,'lxml')
    title=soup.find(attrs={'class':'page-header'}).h1.string
    content=''.join([''.join(list(i.strings)) for i in soup.find(attrs={
        'id':'artibody'}).find_all(attrs={'align':'justify'})])
    ctime=list(soup.find(attrs={'class':'time-source'}).strings)[0].strip()
    source = list(soup.find(attrs={'class': 'time-source'}).strings)[1].strip()
    return {'title':title,'content':content,'ctime':ctime,'source':source}

def sace_to_csv(all_data):
    pd.DataFrame(all_data).to_csv('temp.csv',encoding='utf-8',index=False)
    print("文件保存完毕")

if __name__=='__main__':
    page_num=5
    base_url='https://travel.sina.com.cn/interface/2018_feed.d.json? target=3&page={}'
    all_news_urls=[]
    all_data=[]
    for i in range (1,page_num+1):
        print("开始爬取第{}页-----------------".format(i))
        page_url=base_url.format(i)
        news_urls=get_new_urls(page_url)
        if news_urls:
            for news_url in news_urls:
                print(news_urls)
                data=get_one_news(news_url)
                if data:
                    all_data.append(data)
    print("爬取总共新闻",len(all_data),'条！')
    sace_to_csv(all_data)