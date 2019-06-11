from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import dbConnector
import jieba
import jieba.posseg as pseg
import re

pattern_ED = re.compile(r'[A-Za-z]+')
pattern_CN = re.compile(r'[\u4e00-\u9fa5]+')

#text = 'I\'m a test is really a good test 汉字测试 测试 我是一个简单的测试语句,这个可能会长一点'
text = ''
i = 0
for item in dbConnector.getInfo():
    for note in pattern_ED.findall(item):
        text+= str(note) + ' '
        print('获得关键字: [' + str(note) + '], 关键字总个数: ' + str(i)+ '\n')
        i+=1
print(text);
print('开始生成词图, 请耐心等待');



wordcloud = WordCloud(background_color="white", width=1920, height=1080, margin=1, max_words=20000, collocations=False).generate_from_text(text)
#, font_path="YaHei.Consolas.1.12_0.ttf"
#plt.imshow(wordcloud, interpolation='bilinear')
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
wordcloud.to_file('test.png')
#todo
