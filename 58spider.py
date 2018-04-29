import requests
# import re
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
path = 'D:\chromedriver\chromedriver.exe'
mainURL = 'http://nt.58.com/zptaobaotuiguang/?PGTID=0d202408-0018-afba-ca68-482ac7a3741e&ClickID=2'

driver = webdriver.Chrome(executable_path=path)
driver.get(mainURL)

list = []

def getTextByClass(className, selectType = 'single'):
    tagText = ''
    for tag in driver.find_elements_by_class_name(className):
        if(selectType == 'single'):
            tagText = tag.text
        else: 
            tagText += tag.text + '|'
    return tagText

def toNextPage():
    nextPage = driver.find_elements_by_class_name('next')
    for btn in nextPage:
        btn.click()

def isEnd():
    if(getTextByClass('cur_page') == getTextByClass('total_page')):
        return True
    else:
        return False

def getListURL():
    list_con = driver.execute_script("return $('.job_name a')")
    for item in list_con:
        list.append(item.get_attribute("href"))  

def getDetailInfo():
    compName = getTextByClass('comp_baseInfo_title')
    posTitle = getTextByClass('pos_title')
    posName = getTextByClass('pos_name')
    welfare = getTextByClass('pos_welfare_item', 'all')
    condition = getTextByClass('item_condition', 'all')
    area = getTextByClass('pos_area_item', 'all')
    salary = getTextByClass('pos_salary')

    print(compName+'\n---'+posTitle+'\n---'+posName+'\n---'+welfare+'\n---'+condition+'\n---'+area+'\n---'+salary)

while(not isEnd()):
    getListURL()
    toNextPage()

getListURL()

for page in list:
    driver.get(page)
    getDetailInfo()



driver.close()
