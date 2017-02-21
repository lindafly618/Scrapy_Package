import scrapy

class Movie(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    rating = scrapy.Field()
    ranking = scrapy.Field()
    year = scrapy.Field()
    pass