#-*- coding: utf-8 -*-
import scrapy
import logging
import re 
import simplejson as sj
from unidecode import unidecode

class Movie(object):
	def __str__(self):
		return ', '.join(['{key}={value}'.format(key=key, value=self.__dict__.get(key)) for key in self.__dict__])

	def todict(self):
		return dict(
				name=self.name,
				rating=self.rating,
				year=self.year,				
				duration=self.duration,
				country=self.country,
				directors=self.directors,
				summary=unidecode(self.summary),
				actors=self.actors,
				producer=self.producer,
				photography=self.photography,
				musicians=self.musicians,
				images=self.images,
				guionists=self.guionists,
				genres=self.genres,
				awards=self.awards,
			)

class FilmDataSpider(scrapy.Spider):
	logger = logging.getLogger('FilmDataSpider')

	name = 'filmdataspider'
	url  = 'https://www.filmaffinity.com'
	
	#custom_settings = {
    #   'FEED_FORMAT' : 'csv',
    #   'FEED_URI' : 'tmp/imdb.csv'
   	#}

	def __init__(self, film_id='', *args, **kwargs): 
		super(FilmDataSpider, self).__init__(*args, **kwargs) 
		self.start_urls = ['https://www.filmaffinity.com/es/film{0}.html'.format(film_id)] 
	
	def parse(self, response):
		logger = logging.getLogger('parse')
		
		movie = Movie()

		movie.rating = dict(
					note=float(response.css('#movie-rat-avg::text').get().strip().replace(",", ".")),
					critics=int(response.css('[itemprop="ratingCount"]::text').get().strip().replace(".", ""))
			)

		movie.name = response.css('.movie-info dd::text')[0].get().strip()
		movie.year = response.css('.movie-info dd::text')[1].get().strip()
		movie.duration = response.css('.movie-info dd::text')[2].get().strip()
		movie.country  = response.css('.movie-info dd::text')[3].get().strip()

		movie.images = dict(
				small=response.css('[itemprop="image"]::attr(src)').get().strip().replace("mmed", "small"),
				medium=response.css('[itemprop="image"]::attr(src)').get().strip(),
				large=response.css('[itemprop="image"]::attr(src)').get().strip().replace("mmed", "large")
			)

		directors = []
		for director_p in response.css('.movie-info dd')[4].css("a[itemprop='url']"):
			directors.append(dict(
					name=director_p.css('::attr(title)').get(),
					url="%s%s" % (self.url, director_p.css('::attr(href)').get())
				))
		movie.directors = directors

		guionists = []
		for guionist_p in response.css('.movie-info dd')[5].css('.credits .nb span::text'):
			guionists.append(guionist_p.get())		
		movie.guionists = guionists

		musicians = []
		for musician_p in response.css('.movie-info dd')[6].css('.credits .nb span::text'):
			musicians.append(musician_p.get())		
		movie.musicians = musicians

		photography = []
		for photographer_p in response.css('.movie-info dd')[7].css('.credits .nb span::text'):
			photography.append(photographer_p.get())		
		movie.photography = photography

		actors = []
		for actor_p in response.css('.movie-info dd')[8].css("a[itemprop='url']"):
			actors.append(dict(					
					name=actor_p.css("span[itemprop='name']::text").get(),
					url="%s%s" % (self.url, actor_p.css('::attr(href)').get())
				))
		movie.actors = actors

		producer_ = response.css('.movie-info dd')[9].css('.credits .nb span::text').get()
		if '/' in producer_:
			producer = []
			for produc in producer_.split('/'):
				producer.append(produc.strip())
		else:
			producer = [producer_.strip()]
		movie.producer = producer

		genres = []
		for genre_p in response.css('.movie-info dd')[10].css('a'):
			genres.append(dict(					
					name=unidecode(genre_p.css('::text').get()),
					url=genre_p.css('::attr(href)').get()
				))
		movie.genres = genres

		movie.summary = response.css('.movie-info dd[itemprop="description"]::text').get().strip()
		
		awards = [] 
		for award_p in response.css('.movie-info dd.award').css('.margin-bottom'):
			awards.append(dict(					
					name=unidecode(re.search('</a>:(.*)</div>', award_p.extract()).group(1).strip()),
					year=award_p.css('a::text').get(),
					url=award_p.css('a::attr(href)').get()
				))
		movie.awards = awards

		yield movie.todict()