from lxml.html import fromstring, tostring
import sys
import requests
import json
import re
import os
from multiprocessing import Pool

def saveImage(image, fileName, path):
    with open(path + fileName, 'wb') as file:
        file.write(image)
    print(fileName+' download done!')

def requestURL_content(url, decode='utf8'):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.103 Safari/537.36'}
    return requests.get(url = url, headers = headers, timeout=60).content.decode(decode, "ignore")

def processTask(arrImageURL, savePath, No, broNum):
    for i in range(0, len(arrImageURL)):
        if i%broNum != No:
            continue
        imageUrl = arrImageURL[i]
        imageName = os.path.basename(imageUrl)
        
        print(imageUrl)
        try:
            image = requests.get(url=imageUrl, timeout=60).content
            saveImage(image, imageName, savePath)
        except Exception as e:
            print(imageUrl + ' timeout: ' + str(e))
            continue
        

if __name__ == '__main__':
    # 发布windows应用时加上
    # multiprocessing.freeze_support()
    filename = 'url.txt'
    savePath = './img/'
    if(not os.path.exists(savePath)):
        os.makedirs(savePath) 

    arrImageURL = []

    file = open(filename) 
    for line in file.readlines():
        arrImageURL.append(line.strip('\n')) 
    file.close()
    print('processes start')
    p = Pool(10)
    for i in range(10):
        p.apply_async(processTask, args=(arrImageURL, savePath, i, 10))

    p.close()
    p.join()
    print('All subprocesses done.')

    print('------------------------')
    print('the end')
