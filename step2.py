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
driver = webdriver.Chrome('./chromedriver', chrome_options = chrome_options)

driver.get('http://www.baidu.com')


cookie = open('cookie').read().strip()

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

