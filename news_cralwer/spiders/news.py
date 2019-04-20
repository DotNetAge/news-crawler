# -*- coding: utf-8 -*-
from scrapy.spiders import XMLFeedSpider
from ..items import NewsItem


class NewsSpider(XMLFeedSpider):
    name = 'news'
    #allowed_domains = ['www.chinanews.com']
    url = 'http://rss.sina.com.cn/news/world/focus15.xml'
    start_urls = [url]
    iterator = 'iternodes'  # you can change this; see the docs
    itertag = 'item'  # change it accordingly

    def parse_node(self, response, selector):
        item = NewsItem()
        item['title'] = selector.xpath('title/text()').extract_first()
        item['link'] = selector.xpath('link/text()').extract_first()
        item['pub_date'] = selector.xpath('pubDate/text()').extract_first()
        item['desc'] = selector.xpath('description/text()').extract_first()
        return item
