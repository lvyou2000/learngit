import requests
from bs4 import BeautifulSoup
import lxml
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

url_base="https://list.jd.com/list.html?cat=9987,653,655"



resp=requests.get(url=url_base,headers=request_headers)
status_code=resp.status_code
if status_code==200:
    html_text=resp.text
    soup=BeautifulSoup(html_text,'lxml')


    # telephone_imgs=soup.select('div.p-img>a')
    telephone_img_elements=soup.select('div.p-img>a')
    telephone_img_pages=soup.select('div.p-img>a')
    telephone_prices=soup.select('div.p-price>strong>i')
    telephone_introductions=soup.select('div.p-name.p-name-type-3>a>em')
    telephone_neicuns=soup.select('span.p-attribute>span')
    shops=soup.select('span.J_im_icon>a')
    # try:
    # bargains=soup.select('i.good-icons4.J-picon-tips')
    # except:
    #     bargains=['无']



    for telephone_img_element,telephone_img_page,telephone_price,telephone_introduction,telephone_neicun,shop in zip(telephone_img_elements,telephone_img_pages,telephone_prices,telephone_introductions,telephone_neicuns,shops):
        information={
            '手机图片':telephone_img_element.find(name="img").get("src"),
            '手机图片地址':telephone_img_page.get("href"),
            '价格':telephone_price.get_text().strip(),
            '简介':telephone_introduction.get_text().strip(),
            '内存':telephone_neicun.get_text().strip(),
            '商店':shop.get_text().strip(),
            # '优惠':bargain.get_text().strip(),
        }
        print(information)