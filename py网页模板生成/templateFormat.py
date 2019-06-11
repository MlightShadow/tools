import codecs

try:
    f = open('template/index.html', 'r')

    fw = codecs.open('public/index.html', 'w', 'utf-8')
    fw.write(f.read().format(str1=u'字符串1',str2=u'字符串2'))
finally:
    if f:
        f.close()
    if fw:
        fw.close()

        