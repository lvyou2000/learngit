# -*-codeing = utf-8 -*-
# @Time:2021/3/2 21:41
# @Author:吕尤
# @File:demo1.py
# @Software:PyCharm

# 1.爬取网页
# 2.逐一解析数据
# 3.保存数据

import urllib.request
import urllib.error
import re
from bs4 import BeautifulSoup
import xlwt

def main():
    baseurl="https://movie.douban.com/top250?start="
    # 1.爬取网页
    datalist=getData(baseurl)
    savepath=".\\豆瓣电影Top250.xls"
    savedata(datalist,savepath)
    #askurl(baseurl)

#影片详情规则
findlink=re.compile(r'<a href="(.*?)">')#创建正则表达式对象，表示规则（字符串的模式）
#影片图片连接
findImg=re.compile(r'<img.*src="(.*?)">',re.S)
#影片篇名
findtitle=re.compile(r'<span class="title">(.*)</span>')
#影片评分
findrating=re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
#找到评价人数
findjudge=re.compile(r'<span>(\d*)人评价</span>')
#找到概况
findinq=re.compile(r'<span class="inq">(.*)</span>')
#找到影片相关内容
findbd=re.compile(r'<p class="">(.*)</p>',re.S)


#得到指定一个url的网页内容
def askurl(url):
    head = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.81"}
    request = urllib.request.Request(url=url,headers=head)
    html=""
    try:
        response=urllib.request.urlopen(request)
        html=response.read().decode("utf-8")
        #print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html

def getData(baseurl):
    datalist=[]
    for i in range(0,10):
        url=baseurl+ str(i*25)
        html = askurl(url)

        # 2.逐一解析数据
        soup=BeautifulSoup(html,"html.parser")
        for item in soup.find_all('div',class_="item"):#查找符合要求的字符串形成列表
            data=[]#保存一部电影的所有信息
            item=str(item)

            #获取影片详情的超链接
            link=re.findall(findlink,item)[0]#re库用来通过正则表达式查找指定字符串
            data.append(link)
            #获取图片
            imgsrc=re.findall(findImg,item)[0]
            data.append(imgsrc)
            #获取题目
            titles=re.findall(findtitle,item)
            if len(titles)==2:
                ctitle=titles[0]
                data.append(ctitle)
                otitle=titles[1].replace("/","")#去除无关符号
                data.append(otitle)
            else:
                data.append(titles[0])
                data.append(' ')
            #获取评分
            rating=re.findall(findrating,item)[0]
            data.append(rating)
            #获取评价人数
            judgenum=re.findall(findjudge,item)[0]
            data.append(judgenum)
            #添加概述
            inq=re.findall(findinq,item)
            if len(inq)!=0:
                inq=inq[0].replace("。","")
                data.append(inq)
            else: data.append("")

            bd=re.findall(findbd,item)[0]
            bd=re.sub('<br(\s+)?/>(\s+)?'," ",bd)#去掉br（替换）
            bd=re.sub('/'," ",bd)#去掉/
            data.append(bd.strip())#去掉空格

            datalist.append(data)#将处理好的一部电影信息放入datalist中

            #print (link)

    return datalist



# 3.保存数据
def savedata(datalist,savepath):
    book=xlwt.Workbook(encoding="utf-8",style_compression=0)
    sheet=book.add_sheet('豆瓣电影评分top250',cell_overwrite_ok=True)
    col=("电影详情链接","图片链接","影片中文名","影片外国名","评分","评价数","概况","相关信息")
    for i in range(0,8):
        sheet.write(0,i,col[i])#列名
    for i in range(0,250):
        print("第%d条"%(i+1))
        data=datalist[i]
        for j in range(0,8):
            sheet.write(i+1,j,data[j])
    book.save(savepath)#保存文档


if __name__=="__main__":
    main()
    print("over")