import scrapy

class testspider(scrapy.Spider):
    name="testspider"
    request_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/91.0.4472.124 Safari/537.36'
    }

    start_urls=["https://movie.douban.com/top250?start=0"]

    # 重写方法实现请求发送
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url,callback=self.parse,headers=self.request_headers)
    #重写方法定位提取
    def parse(self, response):
        #对response进行提取定位
        for item in response.css('div.item'):
            yield {
                "filmname":item.css('div.info>div.hd>a>span.title::text').extract_first(),
                "score":item.css('div.info>div.bd>div.star>span.rating_num::text').extract(),
                "introduction":item.css('div.info>div.bd>p.quote>span.inq::text').extract()

            }

        next_url=response.css('div.paginator>span.next>a::attr(href)').extract()
        if next_url:
            next_url="https://movie.douban.com/top250"+next_url[0]
            print(next_url)
            yield scrapy.Request(next_url,headers=self.request_headers)