import requests

# 根据URL访问获取资源CONTENT
def scout(url, decode='utf8'):
    print('do scout: %s', url)
    # 伪装成浏览器
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.103 Safari/537.36'}
    # 带Referer 伪装浏览器
    # headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.103 Safari/537.36', 'Referer':url}

    return requests.get(url = url, headers = headers, timeout=60).content.decode(decode, "ignore")

if __name__ == '__main__':
    print(scout('http://www.baidu.com', 'gbk'))