import scrapy


class RatingsSpider(scrapy.Spider):
    name = "ratings"

    
    start_urls = ['http://www.imdb.com/chart/top']
    
    def parse(self, response):
        for row in response.css('tr')[1:-2]:
            yield {
                'title': row.css('a::text').extract()[2],
                'rating': row.css('strong::text').extract_first()
            }