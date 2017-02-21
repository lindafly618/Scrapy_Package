# -*- coding: utf-8 -*-
import scrapy


class FirstspiderSpider(scrapy.Spider):
    name = "firstspider"
    allowed_domains = ["firstspider.com"]
    start_urls = ['http://firstspider.com/']

    def parse(self, response):
        pass
