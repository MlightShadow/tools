############################
# 通用爬虫脚本             #
############################

############################
# 半自助爬虫脚本
# * 自己修改部分脚本快速书写自己需要的爬虫脚本
# * 获取部分可以通过浏览器获取 xpath 得到   
############################
__version__ = 'v0.1'

import requests
import json
from lxml import etree

from requests.cookies import RequestsCookieJar


def requestWithCookies(cookies):
    requests_session = requests.session()  
    response_captcha = requests_session.get(url='http://localhost/ZhongYou/Admin/Home', cookies=cookies)
    print(response_captcha.content.decode())

def requestLogin():
    requests_session = requests.session() 
    response = requests_session.post(url='http://localhost/ZhongYou/Admin/Login/Login', data=
    {'name': 'admin', 'password': 'admin'}) 
    
    return response.cookies


# 根据URL访问获取资源CONTENT
def requestURL_content(url):
    # 伪装成浏览器
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.103 Safari/537.36'}
    # 带Referer 伪装浏览器 
    # headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.103 Safari/537.36', 'Referer':url}
    
    return requests.get(url = url, headers = headers).content.decode()

# json处理方法
def jsonHandler(content):
    # 这里去掉了get跨域返回的callback函数
    jsonstr = content[content.find('(') + 1:-2]

    dict_json = json.loads(jsonstr)
    return dict_json

# html处理方法
def htmlHandler(content, xpath, attr='text'):
    tags = etree.HTML(content).xpath(xpath)
    elem = []
    for tag in tags: 
        if attr == 'text':
            elem.append(tag.text)
        else: 
            elem.append(tag.attrib.get(attr))
    return elem

if __name__ == "__main__":
    print('commSpiderDemo version:' + __version__ + ' starting ...')
    # html = htmlHandler(requestURL_content('http://www.runoob.com/python/att-list-append.html'), '//*[@id="content"]/h2[1]')
    # json = jsonHandler(requestURL_content('https://sp0.baidu.com/5a1Fazu8AA54nxGko9WTAnF6hhy/su?wd=adm&json=1&p=3&sid=1429_21092_18560_27401_27376&req=2&pbs=administrator&csor=3&pwd=admi&cb=jQuery110206582600666972298_1542005208743&_=1542005208754'))
    # print(html, json)

    

    ############################
    # 通过htmlHandler 和 jsonHandler
    # 可以得到处理后的 json转换后的dict对象, html中解析到的list
    ############################
    cookie_jar = RequestsCookieJar()
    cookie_jar.set('ASP.NET_SessionId', 'mt1uwrw31s0djwatmrlcglre', domain='localhost')
    # requestWithCookies(cookie_jar)
