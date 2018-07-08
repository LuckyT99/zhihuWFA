from pylab import *
from matplotlib.font_manager import *
import matplotlib
import numpy as np

f = open('words.txt', 'r', encoding='utf-8')
lines = []
while True:
    line = f.readline()
    lines.append(line.strip('\n'))
    # 零长度指示 EOF
    if len(line) == 0:
        break
# 关闭文件
f.close()
ab = {}
# 添加一对键值—值配对
for it in lines:
    if it in ab:
        ab[it] += 1
    else:
        ab[it] = 1
print(sorted(ab.items(), key=lambda e: e[1], reverse=True)[0:10:1])

List = sorted(ab.items(), key=lambda e: e[1], reverse=True)[0:10:1]
frequency = []
words = []
for item in List[::-1]:
    words.append(item[0])
    frequency.append(item[1])

topn = frequency[9]
print(frequency)

rcParams['axes.unicode_minus'] = False

myfont = FontProperties(fname='msyh.ttc')
barh(range(10), frequency, height=0.7, color='steelblue', alpha=0.8)  # 从下往上画
yticks(range(10), words, fontproperties=myfont)
i = 0
for x, y in enumerate(frequency):
    text(y + 0.2, x - 0.1, "%s" % frequency[i])
    i = i + 1
xlim(1, topn+10)
xlabel(u"频率", fontproperties=myfont)
title(u"Top10词语", fontproperties=myfont)

savefig("result.png")
#show()
