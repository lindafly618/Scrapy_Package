from scrapy.exceptions import DropItem

class DropMoviePipeline(object):

    def process_item(self, movie, spider):
        if int(movie['year']) > 2000:
            return movie
        else:
            raise DropItem("Movie \' %s \' is before year 2000" % movie['title'])