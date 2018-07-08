# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import jieba

class ZhihuwfaPipeline(object):
    def createstoplist(stoppath):
        #print('load stopwords...')
        stoplist = [line.strip() for line in open(stoppath, 'r', encoding='utf-8').readlines()]
        stopwords = {}.fromkeys(stoplist)
        return stopwords
    def process_item(self, item, spider):
        list=jieba.cut(item['content'],cut_all=False)
        stop = createstoplist("停用词表.txt")
        list2=[]
        for i in list:
            if i in stop:
                continue
            else:
                list2.append(i)
        f=open("分词.txt","w",encoding="utf-8")
        f.write(" ".join(list2))
        return item
