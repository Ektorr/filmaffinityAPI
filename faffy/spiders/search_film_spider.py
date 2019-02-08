# -*- coding: utf-8 -*-
import scrapy
import re
from copy import copy
from unidecode import unidecode

class FaffySearchSpider(scrapy.Spider):
    name = 'faffy_search_spider'

    def __init__(self, film_id='', *args, **kwargs): 
        super(FaffySearchSpider, self).__init__(*args, **kwargs) 
        self.start_urls = ['https://www.filmaffinity.com/es/movietopic.php?topic=461156&attr=all&p=2&order=BY_YEAR&nodoc&limit=150'] 
    
    def parse(self, response, **kwargs):
        response_url = response.request.url

        id_movies = []

        if response.meta.get('id_movies'):
            id_movies = response.meta.get('id_movies')

        try:
            limit = int(re.search('limit=(.*)', response.request.url).group(1).strip())
        except:
            limit = 1


        if '.html' in response_url:
            id_movies.append(re.search('/film(.*).html', response_url).group(1).strip())

        for movie_p in response.css('.movie-card'):
            if len(id_movies) < limit or limit == 0:
                id_movies.append(int(movie_p.css('::attr(data-movie-id)').get()))
            else:
                break

        if len(id_movies) < limit or limit == 0:
            n_next_page = response.xpath("//div[contains(@class, '%s')]/span[contains(@class, '%s')]/following-sibling::a[1]/@href" % (u'pager', u'current')).extract_first()
            if n_next_page: 
                href = "%s&limit=%s" % (n_next_page, limit)
                yield scrapy.Request(href, callback=self.parse, meta={'id_movies': id_movies})

        yield {'movies':  id_movies} 