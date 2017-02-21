import scrapy

class MySpider(scrapy.Spider):
    name = 'faulty'
    allowed_domains = ['simon.rochester.edu']
    start_urls = ['http://www.simon.rochester.edu/faculty-and-research/faculty-directory/index.aspx']