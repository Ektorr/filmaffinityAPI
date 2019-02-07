# -*- coding: utf-8 -*-
import scrapy
import re
from unidecode import unidecode

class FaffySearchSpider(scrapy.Spider):
    name = 'faffy_search_spider'

    def __init__(self, film_id='', *args, **kwargs): 
        super(FaffySearchSpider, self).__init__(*args, **kwargs) 
        self.start_urls = ['https://www.filmaffinity.com/es/search.php?stype=title&stext=las%20aventuras%20de%20brandy'] 
    
    def parse(self, response):
        
        response_url = response.request.url

        if '.html' in response_url:
            id_movies = [re.search('/film(.*).html', response_url).group(1).strip()]
        else:
            id_movies = []

        for movie_p in response.css('.movie-card'):
            id_movies.append(movie_p.css('::attr(data-movie-id)').get())

        yield {'movies': id_movies }