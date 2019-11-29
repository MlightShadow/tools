import looter
import scouter
from lxml import etree

def run(urls, target, action):
    for url in urls:
        resp = scouter.scout(url, 'gbk')
        elem = htmlHandler(resp, target)
        looter.loot(elem, action)

# html处理方法
def htmlHandler(content, xpath):
    tags = etree.HTML(content).xpath(xpath)
    elem = []
    for tag in tags:
    	elem.append(tag)
    return elem

if __name__ == '__main__':
    urls = [''];
    run(urls, '/html/body/div[2]/div[3]/div[1]/div[1]/div[2]/h4/strong/a/@href', 'src')