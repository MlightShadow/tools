import os
import codecs

def file_name(path):
    htmlheader=''' <!DOCTYPE html> 
            <html>
            <head>
                <meta charset="utf-8" />
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <title>custom</title>
                <meta content="width=device-width, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, user-scalable=no" name="viewport">
                <style>
                img {
                    max-width:100%

                }
                </style>
            </head>
            <body>
                '''
    htmlfooter='''
            </body>
            </html>
            '''

    pageNum = 10000
    indexHtml = htmlheader
    for dirpath,dirnames,filenames in os.walk(path):
        htmlName = str(pageNum)
        try:
            fw = codecs.open(htmlName +'.html', 'w', 'utf-8')
            strhtml = htmlheader
            for filename in filenames:
                strhtml +='<img src="{str1}" /><br/>'.format(str1=str(os.path.join(dirpath,filename)))
            strhtml += htmlfooter
            fw.write(strhtml)
        finally:
            if fw:
                fw.close()
        indexHtml += '<a href="{str0}">{str1}</a><br/>'.format(str0=(htmlName+'.html'), str1=htmlName) + htmlfooter
        pageNum +=1
    try:
        fw = codecs.open('index.html', 'w', 'utf-8')
        fw.write(indexHtml)
    finally:
        if fw:
            fw.close()

file_name('.')
