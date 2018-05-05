import requests
from bs4 import BeautifulSoup
from html.parser import HTMLParser
import time
import re


def getSoup(url):
    return BeautifulSoup(requests.get(url).text, 'html.parser')

def getNextPage(soup, prefixURL):
    nextPage = soup.find_all('a',class_='next', attrs={'href': True})
    nextLink = ''
    for link in nextPage:
        nextLink = link['href']
    if(nextLink != ''):
        nextLink = prefixURL + nextLink
    return nextLink

def getJobList(soup):
    jobList = soup.find_all('a',class_='list_title')
    num = 0
    for link in jobList:
        list.append(link['href'])
        num += 1
    return num

def getTextByClass(soup, className):
    tagText = ''
    for tag in soup.find_all(class_ = className):
        for string in tag.stripped_strings:
            tagText += (( '' if tagText == '' else ',') + str(string).replace('\r', '').replace('\t', '').replace('\n', ''))
    return tagText

def getDetail(soup):
    compName = getTextByClass(soup,'company-info')
    posTitle = getTextByClass(soup,'title-line')
    posName = getTextByClass(soup,'title-line')
    welfare = getTextByClass(soup,'welfare-line')
    condition = getTextByClass(soup,'description-label')
    area = getTextByClass(soup,'location-line')
    salary = getTextByClass(soup,'salary-line')

    print(compName)
    time.sleep(0.05)
    print('\n---'+posTitle)
    time.sleep(0.05)
    print('\n---'+posName)
    time.sleep(0.05)
    print('\n---'+welfare)
    time.sleep(0.05)
    print('\n---'+condition)
    time.sleep(0.05)
    print('\n---'+area)
    time.sleep(0.05)
    print('\n---'+salary)
    time.sleep(0.05)


if __name__ == '__main__':
    #mainURL = input('请输入起始URL\n')
    mainURL = 'http://nantong.ganji.com/zpqichexiaoshou/'
    list = []
    scanNum = 0
    readNum = 0
    pageLink = mainURL
    end = pageLink.index('.com') + 4
    prefixURL = pageLink[0 : end]
    print('扫描开始' + prefixURL)

    while(pageLink != ''):
        print(pageLink)
        soup = getSoup(pageLink)
        scanNum += getJobList(soup)
        print('总计链接数:' + str(scanNum))
        pageLink = getNextPage(soup, prefixURL)

    for item in list:
        print(item)
        time.sleep(0.05)
        soup = getSoup(item)
        getDetail(soup)
        readNum += 1
        print('总计链接数:' + str(scanNum) + ' 当前扫描:' + str(readNum) + ' 进度:' + str(round(readNum/scanNum * 100, 2) )+'%')
        time.sleep(0.05)


    print('扫描完成')