import requests
from bs4 import BeautifulSoup
import lxml
import time
import random
import csv
import re

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
url_str = "https://movie.douban.com/review/best/?start="


def get_content(content):
    web_data = requests.get(url=content, headers=request_headers)
    status_code = web_data.status_code
    if status_code == 200:
        html_text = web_data.text
        soup = BeautifulSoup(html_text, "html.parser")
        targets=soup.select('#link-report>div>p')

        x=""
        for target in targets:
            x=x+target.get_text().strip()
        return x




urls = ['https://movie.douban.com/review/best/?start={}'.format(str(no)) for no in range(0, 100, 20)]
for url_str in urls:

    resp = requests.get(url=url_str, headers=request_headers)

    status_code = resp.status_code
    if status_code == 200:
        html_text = resp.text

    # soup=BeautifulSoup(html_text,"html.parser")# 内置解析器
    soup = BeautifulSoup(html_text, "lxml")  # 内置解析器

    # author_name_element=soup.find(name='a', class='name')
    # author_name_element=soup.find(name='a', herf="https://www.douban.com/people/184234641/")
    # author_name_element=soup.find_all(name='header',class='main_hd')

    # author_info_element=soup.select_one('a.name')
    # author_info_element=soup.select_one('header.main_hd')

    author_info_elements = soup.select('a.name')
    author_info_elements2 = soup.select('a.avator')
    movie_info_elements = soup.select('a.subject-img')
    evaluate_times = soup.select('span.main-meta')
    p_agrees = soup.select('div.action>a.action-btn.up>span')
    p_disagrees = soup.select('div.action>a.action-btn.down>span')
    p_replys = soup.select('div.action>a.reply')
    # if soup.select('span.allstar50.main-title-rating'):
    #     score=5

    titles=soup.select('div.main-bd>h2>a')
    # evaluate_score=soup.select('span.allstar\d+main-title-rating')

    evaluate_scores=soup.select("header>span:nth-of-type(1)")


    # evaluate_score = 0
    # try:
    #     evaluate_scores=soup.select("header>span:nth-of-type(1)").get("title")
    # except:
    #     evaluate_score = 0
    # print(evaluate_score)


    # 提取作者名字、主页；图片地址、电影名称
    # for author_info_element in author_info_elements:
    #     author_name=author_info_element.get_text().strip()
    #     author_homepage=author_info_element.get('href')
    #     print(author_name,author_homepage)

    for author_info_element, author_info_element2, movie_info_element,evaluate_time,evaluate_score,title,p_agree, p_disagree, p_reply \
            in zip(author_info_elements, author_info_elements2, movie_info_elements, evaluate_times,evaluate_scores,titles, p_agrees,
                   p_disagrees, p_replys):

        score="no"
        try:
            score=evaluate_score.get("title")
        except:
            score="no"
        movie_info_img_element = movie_info_element.find(name="img")
        author_name = author_info_element.get_text().strip()
        author_homepage = author_info_element.get('href')
        author_img = author_info_element2.find(name="img").get('src')
        movie_name = movie_info_img_element.get("title")
        movie_homepage = movie_info_element.get("href")
        movie_cover_img = movie_info_img_element.get('src')
        time = evaluate_time.get_text()
        cont=title.get_text().strip()
        content=title.get("href").strip()
        x=get_content(content)
        agree = p_agree.get_text().strip()
        disagree = p_disagree.get_text().strip()
        reply = p_reply.get_text().strip()

        # 生成字典，整体放入信息
        movie_review_info = {
            'author_name': author_name,
            'author_homepage': author_homepage,
            'author_img': author_img,
            'movie_name': movie_name,
            'movie_homepage': movie_homepage,
            'movie_cover_img': movie_cover_img,
            'score':score,
            'time': time,
            'title':cont,
            'content':x,
            'agree': agree,
            'disagree': disagree,
            'reply': reply
        }
        row2 = [author_name, author_homepage, author_img, movie_name, movie_homepage, movie_cover_img,score,time,
                cont,x,agree,disagree,reply]
        out = open("影评.csv", "a", newline="", encoding="utf-8")
        csv_writer = csv.writer(out)
        csv_writer.writerow(row2)
        print(movie_review_info)
