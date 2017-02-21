import scrapy
from scrapy.selector import HtmlXPathSelector

class MySpider(scrapy.Spider):
    name = 'faulty'
    allowed_domains = ['simon.rochester.edu']
    start_urls = ['http://www.simon.rochester.edu/faculty-and-research/faculty-directory/index.aspx'
                 ]
    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        titles = hxs.xpath("//td[@class='name']")
        for title in titles:
            name = title.select("a/text()").extract()
            link = title.select("a/@href").extract()
            print (title, link)