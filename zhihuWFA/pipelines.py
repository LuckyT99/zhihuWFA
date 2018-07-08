# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import jieba


def createstoplist(stoppath):
    #print('load stopwords...')
    stoplist = [line.strip() for line in open(
        stoppath, 'r', encoding='utf-8').readlines()]
    stoplist.append(' ')
    stopwords = {}.fromkeys(stoplist)
    return stopwords


class ZhihuwfaPipeline(object):

    def process_item(self, item, spider):
        list = jieba.cut(item['content'], cut_all=False)
        stop = createstoplist("stopWords.txt")
        f = open("words.txt", "a+", encoding="utf-8")
        for i in list:
            if i in stop:
                continue
            else:
                f.write(i + '\n')
        return item
