# -*- coding: utf-8 -*-
import scrapy
import re
from unidecode import unidecode

class FaffyTopichSpider(scrapy.Spider):
    name = 'faffy_topic_spider'

    def __init__(self, film_id='', *args, **kwargs): 
        super(FaffyTopichSpider, self).__init__(*args, **kwargs) 
        self.start_urls = ['https://www.filmaffinity.com/es/topics.php'] 
    
    def parse(self, response):

        topics = []

        for topic_p in response.css('.topic'):
            url = topic_p.css('::attr(href)').get()

            topics.append(
                    dict(
                        id=re.search('topic=(.*)&nodoc', url).group(1).strip(),
                        name=unidecode(topic_p.css('::text').get().strip()),
                        films=int(topic_p.css('em::text').get().replace('(', '').replace(')', '')),
                        href=url
                        )
                )

        yield {'topics': topics }