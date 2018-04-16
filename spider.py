import requests
import re
from bs4 import BeautifulSoup
from selenium import webdriver
path = "D:\chromedriver\chromedriver.exe"



driver = webdriver.Chrome(executable_path=path)
driver.get('https://manhua.dmzj.com/yiquanchaoren/25445.shtml#@page=1')
html = driver.page_source

bs=BeautifulSoup(html)
print (bs.find(attrs={'name':re.compile(r'page_\d+')}))

btnNext = driver.find_elements_by_class_name("img_land_next")
for btn in btnNext:
    btn.click()

driver.get(driver.current_url)

html = driver.page_source

bs=BeautifulSoup(html)
print (bs.find(attrs={'name':re.compile(r'page_\d+')}))


# r  = requests.get('https://manhua.dmzj.com/yiquanchaoren/25445.shtml#@page=1')



driver.close()

# print (bs.find_all('page_1'))
# print (bs.select('img'))