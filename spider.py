import requests
# import re
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
path = 'D:\chromedriver\chromedriver.exe'
mainURL = 'https://manhua.dmzj.com/yiquanchaoren/25445.shtml#@page=1'
picDir = 'C:\\Users\\Z47\\Desktop\\picDir'



global i 

def getImageURL(driver, url):
    global i 
    driver.get(url)
    for imagelink in driver.find_elements_by_tag_name('option'):
        url = 'https:'+ imagelink.get_attribute('value')
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
        headers['Referer'] = driver.current_url
        print(url)
        html = requests.get(url, headers=headers)
        print(html)
        image = html.content
        with open(picDir+ '/' + str(i) + '.jpg', 'wb') as file:
            file.write(image)

        # f = open( picDir+ '/' + str(i) + '.jpg',"wb")
        # headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
        # headers['Host'] = 'https://manhua.dmzj.com'
        # req=urllib.request.Request(url = 'https:'+ url, headers = headers )
        # response = urllib.request.urlopen(req)
        # buf = response.read()
        # f.write(buf)

        i = i + 1

    # bs=BeautifulSoup(driver.page_source)
    # print (bs.find(attrs={'name':re.compile(r'page_\d+')}))

i = 0
driver = webdriver.Chrome(executable_path=path)

getImageURL(driver, mainURL)

loginTip = driver.find_elements_by_class_name('login_tip')
for tip in loginTip:
    tip.click()

while(True):
    btnNext = driver.find_elements_by_class_name('fr')
    for btn in btnNext:
        btn.click()

    getImageURL(driver, driver.current_url)
    
driver.close()