# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from html.parser import HTMLParser
import time
import dbConnector

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
    insert_data = {
        'compName' : getTextByClass(soup,'comp_baseInfo_title'),
        'posTitle' : getTextByClass(soup,'pos_title'),
        'posName' : getTextByClass(soup,'pos_name'),
        'posAddress' : getTextByClass(soup,'pos-area'),
        'posSalary': getTextByClass(soup,'pos_salary'),
        'posWelfare' : getTextByClass(soup,'pos_welfare_item'),
        'posConditionLabel' : getTextByClass(soup,'item_condition'),
        'posConditionDetail' : getTextByClass(soup,'posDes'),
        'posCompDetail' : getTextByClass(soup,'comIntro'),
        'url' : url
    }
    print(insert_data.get('compName'))
    print('\n---'+insert_data.get('posTitle'))
    print('\n---'+insert_data.get('posName'))
    print('\n---'+insert_data.get('posAddress'))
    print('\n---'+insert_data.get('posSalary'))
    print('\n---'+insert_data.get('posWelfare'))
    print('\n---'+insert_data.get('posConditionLabel'))
    print('\n---'+insert_data.get('posConditionDetail'))
    print('\n---'+insert_data.get('posCompDetail'))
    print('\n---'+insert_data.get('url'))

    dbConnector.executeSQL(insert_data)

if __name__ == '__main__':
    #mainURL = input('请输入起始URL\n')
    mainURL = 'http://nt.58.com/job/'
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
        try:
            print(item)
            time.sleep(0.5)
            soup = getSoup(item)
            getDetail(soup, item)
            readNum += 1
            print('总计链接数:' + str(scanNum) + ' 当前扫描:' + str(readNum) + ' 进度:' + str(round(readNum/scanNum * 100, 2) )+'%')
        except Exception as e:
            continue



    print('扫描完成')