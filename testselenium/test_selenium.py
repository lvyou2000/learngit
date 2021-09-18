# 导入 selenium
from selenium import webdriver

browser = webdriver.Chrome()

url_str = "https://www.baidu.com"

browser.get(url_str)

input_text = browser.find_element_by_id("kw")
input_text.send_keys("天津")
search_btn = browser.find_element_by_id("su")
search_btn.click()

browser.sa