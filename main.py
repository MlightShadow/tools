from urllib import request

def doRequest(url, data, method):
    response = request.urlopen(url)
    page = response.read().decode('utf-8')
    return page

	
def main():
    url = input('input url')
    print (doRequest(url, None, None))



main()