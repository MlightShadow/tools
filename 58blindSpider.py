import requests
from bs4 import BeautifulSoup
from html.parser import HTMLParser
import time
import re

def getSoup(url):
    return BeautifulSoup(requests.get(url).text, 'html.parser')

def getNextPage(soup):
    nextPage = soup.find_all('a',class_='next', attrs={'href': True})
    nextLink = ''
    for link in nextPage:
        nextLink = link['href']
    return nextLink

def getJobList(soup):
    jobList = soup.find_all('div',class_='job_name')
    num = 0
    for link in jobList:
        list.append(link.a['href'])
        num += 1
    return num

def getTextByClass(soup, className):
    tagText = ''
    for tag in soup.find_all(class_ = className):
        for string in tag.stripped_strings:
            tagText += (( '' if tagText == '' else ',') + str(string).replace('\r', '').replace('\t', '').replace('\n', ''))
    return tagText

def getDetail(soup, url):
    compName = getTextByClass(soup,'comp_baseInfo_title')
    posTitle = getTextByClass(soup,'pos_title')
    posName = getTextByClass(soup,'pos_name')
    welfare = getTextByClass(soup,'pos_welfare_item')
    condition = getTextByClass(soup,'item_condition')
    area = getTextByClass(soup,'pos_area_item')
    salary = getTextByClass(soup,'pos_salary')

    print(compName)
    print('\n---'+posTitle)
    print('\n---'+posName)
    print('\n---'+welfare)
    print('\n---'+condition)
    print('\n---'+area)
    print('\n---'+salary)

if __name__ == '__main__':
    mainURL = input('请输入起始URL\n')
    #mainURL = 'http://nt.58.com/tech/?PGTID=0d202408-0018-a194-29f2-6653f2972429&ClickID=4'
    list = []
    scanNum = 0
    readNum = 0
    pageLink = mainURL
    print('扫描开始')

    while(pageLink != ''):
        print(pageLink)
        soup = getSoup(pageLink)
        scanNum += getJobList(soup)
        print('总计链接数:' + str(scanNum))
        pageLink = getNextPage(soup)

    for item in list:
        print(item)
        time.sleep(0.5)
        soup = getSoup(item)
        getDetail(soup, item)
        readNum += 1
        print('总计链接数:' + str(scanNum) + ' 当前扫描:' + str(readNum) + ' 进度:' + str(round(readNum/scanNum * 100, 2) )+'%')


    print('扫描完成')