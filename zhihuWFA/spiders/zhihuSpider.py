# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider
from zhihuWFA.items import ZhihuwfaItem


class ZhihuspiderSpider(CrawlSpider):
	name = 'zhihuSpider'
	allowed_domains = ['zhihu.com']

	with open('range.txt', 'r', encoding='UTF-8') as f:
		start_id, end_id = map(int, f.read().split(' '))
	start_urls = ['https://www.zhihu.com/answer/{}'.format(id) for id in range(start_id, end_id + 1)]

	def parse(self, response):
		contents = response.xpath(
			'//*[@id="root"]/div/main/div/div[2]/div[1]/div[2]/div/div/div[2]/div[1]//text()').extract()
		for c in contents:
			item = ZhihuwfaItem()
			item['content'] = c
			yield item
