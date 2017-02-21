import scrapy
from imdbTop.items import Movie

class RatingsSpider(scrapy.Spider):
    name = "ratings_advanced"

    start_urls = ['http://www.imdb.com/chart/top']
    
    def parse(self, response):
        movies = []
        for row in response.css('tr')[1:-2]:
            movie = Movie()
            movie['title'] = row.css('a::text').extract()[2]
            movie['rating'] = row.css('strong::text').extract_first()
            movie['ranking'] = row.css('td.titleColumn::text').extract()[0].replace('\n', '').replace(' ','').replace('.','')
            movie['year'] = row.css('span.secondaryInfo::text').extract()[0][1:-1]
            movies.append(movie)
        return movies