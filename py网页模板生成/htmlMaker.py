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

    try:
        html = htmlheader
        fw = codecs.open('index.html', 'w', 'utf-8')
        for dirpath,dirnames,filenames in os.walk(path):
            for filename in filenames:
                html += '<image src="{str1}" /><br/>'.format(str1=str(os.path.join(dirpath,filename)))
        html += htmlfooter
        fw.write(html)
    finally:
        if fw:
            fw.close()

file_name('.')
