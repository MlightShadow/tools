from urllib import request

class Spider:

    def doRequest(self, url, data, method):
        response = request.urlopen(url)
        page = response.read().decode('utf-8')
        return page

	
    def doMain(self):
        url = input('input url')
        print (self.doRequest(url, None, None))


if __name__ == "__main__":
    spider = Spider()
    spider.doMain()