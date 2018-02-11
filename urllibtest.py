# -*- coding: UTF-8 -*-
from urllib import request
from urllib import parse
import json

if __name__ == "__main__":
    Request_URL = 'https://sp0.baidu.com/5a1Fazu8AA54nxGko9WTAnF6hhy/su?wd=1&json=1&p=3&sid=1430_21101_22157&req=2&csor=1&cb=jQuery110207757729723869495_1518328244378&_=1518328244381'
    Form_Data = {}
    Form_Data['wd'] = '1'
    Form_Data['json'] = '1'
    Form_Data['p'] = '3'
    Form_Data['sid'] = '1430_21101_22157'
    Form_Data['req'] = '2'
    Form_Data['csor'] = '1'
    Form_Data['cb'] = 'jQuery110207757729723869495_1518328244378'
    Form_Data['_'] = '1518328244381'
    data = parse.urlencode(Form_Data).encode('utf-8')
    response = request.urlopen(Request_URL,data)
    html = response.read().decode('utf-8')

    print("%s" % html)