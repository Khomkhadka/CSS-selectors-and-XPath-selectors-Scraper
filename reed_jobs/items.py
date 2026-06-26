# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ReedJobsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    detail_url    = scrapy.Field()   # A. Job page URL
    title         = scrapy.Field()   # B. Job title
    salary        = scrapy.Field()   # C. Salary
    contract_type = scrapy.Field()   # D. e.g. Permanent
    job_type      = scrapy.Field()   # E. e.g. Full-time
    location      = scrapy.Field()   # F. e.g. London
    pass

