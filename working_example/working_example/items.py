
from scrapy.item import Item, Field

class WorkingExampleItem(Item):
    title = Field() # title is the item name
    link = Field() # link is the like to open the item selling information