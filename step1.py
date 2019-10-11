# -*- coding: UTF-8 -*-
import os
import sys
import time
from bs4 import BeautifulSoup
import urlparse
reload(sys)
sys.setdefaultencoding('utf-8')



from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--headless')
#chrome_options.add_argument('referer=https://s.taobao.com/search?q=%E6%B2%99%E5%8F%91&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20191009&ie=utf8&bcoffset=6&ntoffset=6&p4ppushleft=1%2C48&s=0')

driver = webdriver.Chrome('./chromedriver_76', chrome_options = chrome_options)

driver.get('http://www.taobao.com')

cookie = 'cna=02qUEwlwQmMCAXzK4ZrYz90X; t=8c9434a3de7528e536eae14f51d6ba50; thw=cn; tracknick=fnozoszzt; lgc=fnozoszzt; enc=HKXq6WV4oB5%2Brh0%2B8YCfSSZqRCQ3ZYxp5B6YO5ZmLvNbZG5JM79Ua1%2B%2FvlJfaO9Rehztfhb2jWvgZLlCU%2FSbQg%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; miid=1119129829644091141; tg=0; uc3=nk2=Bd6whG%2FB4MY3&vt3=F8dByuHS%2BP0p%2BqNanUQ%3D&id2=VAmslmGYgqeF&lg2=UIHiLt3xD8xYTw%3D%3D; uc4=nk4=0%40B1LQOuthH6zlN7uSksseMJjXy5E%3D&id4=0%40VhCXz%2BB%2Fcy4TKmxy5iierln0kHo%3D; _cc_=VT5L2FSpdA%3D%3D; mt=ci=-1_0; v=0; cookie2=107e2ccba8ef05b40a7e3a4407585894; _tb_token_=e667633e8eedb; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; JSESSIONID=83C165A45DAB59E39CC6D72A2C33518C; uc1=cookie14=UoTbnV5u49SZDw%3D%3D; l=cBgBkNWgvPZl9Y0jBOfwKurza77tNCAffsPzaNbMiIB19m1t1dmwbHwBM-Iwp3QQE95AIexzzRH22RnM-k4_8tgKqelyRs5mp; isg=BCQklqjzJQpnglcLd7jkDCHm9STWFY9BAc_duD5Ble6B6c-zZMxMtVOPqQHUMYB_'

cookie_dict = {}
for s in cookie.split(';'):
    ss = s.strip().split('=', 1)
    cookie_dict[ss[0]] = ss[1]
print '初始化cookie:', cookie_dict





for k in cookie_dict:
    #print 'set', k
    driver.add_cookie({'name': k, 'value': cookie_dict[k], 'path': '/', 'domain': '.taobao.com', 'expires': None})
#print driver

#print driver.title

#wr = open('a.html', 'w')
#print >>wr, driver.page_source

base_url = 'https://s.taobao.com/search?q=%s&imgfile=&js=1&stats_click=search_radio_all%%3A1&initiative_id=staobaoz_20191009&ie=utf8&bcoffset=6&ntoffset=6&p4ppushleft=1%%2C48&s='

word = raw_input('请输入搜索关键词\n')
url = base_url % word + '0'

print 'start url : ' + url

num = 0
while True:
    page = raw_input('请输入页数（1-100）\n')
    try:
        num = int(page)
        if num >= 1 and num <= 100:
            break
        else:
            print '范围不对，请重新输入'
    except:
        print '不合法，请重新输入'

print '抓取' + str(num) + '页'


link_list = []

def index_crawl(idx, url, file_name):
    print '开始抓取第' + str(idx) + '页，链接为' + url
    my_list = []
    driver.get(url)
    time.sleep(5)
    html = BeautifulSoup(driver.page_source)
    d = open(file_name, 'w')
    print >>d, driver.page_source
    item_list = html.find_all(class_ = 'item J_MouserOnverReq')
    print '存储为' + file_name + '，取得所有商品共' + str(len(item_list)) + '件，和下一页链接'
    for s in item_list:
        item2 = s.find(class_ = 'pic')
        if item2 != None and item2.a != None:
            if item2.a['href'] != None:
                link = urlparse.urljoin(url, item2.a['href'])
            print '商品链接：' + link
            my_list.append(link)
    return my_list


link_list += index_crawl(1, url, 'index/1.html')
for i in range(2, num + 1):
    url = base_url % word + str((i - 1) * 44)
    #print '开始抓取第' + str(i) + '页，链接为' + url
    link_list += index_crawl(i, url, 'index/' + str(i) + '.html')
    

wr = open('link.list', 'w')
for s in link_list:
    print >>wr, s

driver.close()
exit(1)



#time.sleep(10)
print data
print >>d, data

"""
driver.execute_script('$(".page-next")[0].click()')
time.sleep(2)
data = html.find(class_ = 'curr-page')
print data

driver.execute_script('$(".page-next")[0].click()')
time.sleep(2)
data = html.find(class_ = 'curr-page')
print data
"""
for i in range(2, 300):
    print '----'
    print driver.find_elements_by_xpath('.//div[@class="turn-next page-next"]')
    print driver.find_elements_by_xpath('.//div[@class="turn-next page-next"]')[0]
    print type(driver.find_elements_by_xpath('.//div[@class="turn-next page-next"]')[0])
    driver.find_elements_by_xpath('.//div[@class="turn-next page-next"]')[0].click()
    time.sleep(2)
    html = BeautifulSoup(driver.page_source)
    data = html.find(class_ = 'page curr-page')
    #print data
    d = open(str(i) + '.html', 'w')
    print >>d, data

driver.close()



#for i in range(2, 178):
    


