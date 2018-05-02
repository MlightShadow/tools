from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = 'I\'m a test is really a good test 汉字测试 测试 我是一个简单的测试语句,这个可能会长一点'

wordcloud = WordCloud(font_path="YaHei.Consolas.1.12_0.ttf").generate(text)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
