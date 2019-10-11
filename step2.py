# -*- coding: UTF-8 -*-
import os
import sys
import time
from bs4 import BeautifulSoup
import urlparse
import requests
reload(sys)
sys.setdefaultencoding('utf-8')

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome('./chromedriver_76', chrome_options = chrome_options)

driver.get('http://www.baidu.com')

cookie = 'cna=02qUEwlwQmMCAXzK4ZrYz90X; t=8c9434a3de7528e536eae14f51d6ba50; thw=cn; tracknick=fnozoszzt; lgc=fnozoszzt; enc=HKXq6WV4oB5%2Brh0%2B8YCfSSZqRCQ3ZYxp5B6YO5ZmLvNbZG5JM79Ua1%2B%2FvlJfaO9Rehztfhb2jWvgZLlCU%2FSbQg%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; miid=1119129829644091141; tg=0; uc3=nk2=Bd6whG%2FB4MY3&vt3=F8dByuHS%2BP0p%2BqNanUQ%3D&id2=VAmslmGYgqeF&lg2=UIHiLt3xD8xYTw%3D%3D; uc4=nk4=0%40B1LQOuthH6zlN7uSksseMJjXy5E%3D&id4=0%40VhCXz%2BB%2Fcy4TKmxy5iierln0kHo%3D; _cc_=VT5L2FSpdA%3D%3D; mt=ci=-1_0; v=0; cookie2=107e2ccba8ef05b40a7e3a4407585894; _tb_token_=e667633e8eedb; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; JSESSIONID=83C165A45DAB59E39CC6D72A2C33518C; uc1=cookie14=UoTbnV5u49SZDw%3D%3D; l=cBgBkNWgvPZl9Y0jBOfwKurza77tNCAffsPzaNbMiIB19m1t1dmwbHwBM-Iwp3QQE95AIexzzRH22RnM-k4_8tgKqelyRs5mp; isg=BCQklqjzJQpnglcLd7jkDCHm9STWFY9BAc_duD5Ble6B6c-zZMxMtVOPqQHUMYB_'

cookie_dict = {}
for s in cookie.split(';'):
    ss = s.strip().split('=', 1)
    cookie_dict[ss[0]] = ss[1]
print '初始化cookie:', cookie_dict
for k in cookie_dict:
    driver.add_cookie({'name': k, 'value': cookie_dict[k], 'path': '/', 'domain': '.taobao.com', 'expires': None})


output = open('output.txt', 'w')

idx = 0
for line in open('link.list'):
    line = line.strip()
    if 'tmall' in line:
        continue
    
    idx += 1
    #if idx > 5:
    #    break


    print >>output, line,
    driver.get(line)
    time.sleep(3)
    wr = open('page/' + str(idx) + '.html', 'w')
    print >>wr, driver.page_source
    page = BeautifulSoup(driver.page_source)
    
    h = page.find(class_ = 'wl-servicemarkinfo')
    text = ''
    if h != None:
        text = page.find(class_ = 'wl-servicemarkinfo').text.strip()



    print >>output, text


driver.close()

