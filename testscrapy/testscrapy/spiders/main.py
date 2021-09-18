from scrapy import cmdline
cmd_param="testspider -o doubanfilm.csv"
cmd_line_str="scrapy crawl {}".format(cmd_param)

cmdline.execute(cmd_line_str.split())