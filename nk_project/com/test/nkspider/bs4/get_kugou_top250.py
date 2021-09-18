from bs4 import BeautifulSoup
import time
import requests


request_headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                 'Chrome/91.0.4472.124 Safari/537.36',
    'Connection':'keep-alive'
}

def get_info(page_url):
    resp=requests.get(url=page_url,headers=request_headers)
    html_text=resp.text
    soup_document=BeautifulSoup(html_text,'lxml')
    ranks=soup_document.select('span.pc_temp_num')
    titles=soup_document.select('div.pc_temp_songlist>ul>li>a')
    # titles=soup_document.select('a.pc_temp_songname')
    # times=soup_document.select('div.pc_temp_songlist>ul>li>span.pc_temp_tips_r>span')
    times=soup_document.select('span.pc_temp_time')
    for rank,title,time in zip(ranks,titles,times):
        if '-' in title.get_text():
            data={
                'rank':rank.get_text().strip(),
                'singer':title.get_text().split('-')[0].strip(),
                'title':title.get_text().split('-')[1].strip(),
                'time':time.get_text().strip()
            }
            print(data)
        else:
            data = {
                'rank': rank.get_text().strip(),
                'singer': title.get_text()[0].strip(),
                'title': title.get_text()[1].strip(),
                'time': time.get_text().strip()
            }
            print(data)

if __name__ =="__main__":
    urls=["https://www.kugou.com/yy/rank/home/{}-8888.html".format(str(i)) for i in range(1,24)]
    for url in urls:
        get_info(url)
        time.sleep(1)
    print("end")