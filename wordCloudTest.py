from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import dbConnector

#text = 'I\'m a test is really a good test 汉字测试 测试 我是一个简单的测试语句,这个可能会长一点'
text = ''
i = 0
for item in dbConnector.getInfo():
    text += item + ' '
    i+=1

print(text)
print(i)

wordcloud = WordCloud(background_color="white", width=3840, height=2160, margin=1, max_words=i, font_path="YaHei.Consolas.1.12_0.ttf").generate(text)

#plt.imshow(wordcloud, interpolation='bilinear')
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
wordcloud.to_file('test.png')
#todo
