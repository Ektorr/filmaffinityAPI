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
				id=self.id,
				name=unidecode(self.name),
				spanish_name=self.spanish_name if self.spanish_name else '',
				rating=self.rating,
				year=self.year,				
				duration=self.duration,
				country=unidecode(self.country),
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
				url=self.url,
			)

class FilmDataSpider(scrapy.Spider):
	logger = logging.getLogger('FilmDataSpider')

	name = 'filmdataspider'
	url  = 'https://www.filmaffinity.com'

	url_trailers = 'https://www.filmaffinity.com/es/evideos.php?movie_id='
	url_reviews  = 'https://www.filmaffinity.com/es/pro-reviews.php?movie-id='
	url_images   = 'https://www.filmaffinity.com/es/filmimages.php?movie_id='
	
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

		movie.url = response.request.url
		
		movie.id = int(re.search('/film(.*).html', movie.url).group(1).strip())

		movie.rating = dict(
					note=float(response.css('#movie-rat-avg::text').get().strip().replace(",", ".")) if response.css('#movie-rat-avg::text').get() else False,
					critics=int(response.css('[itemprop="ratingCount"]::text').get().strip().replace(".", "")) if response.css('[itemprop="ratingCount"]::text').get() else False
			)

		movie.name = response.css('.movie-info dd::text')[0].get().strip()
		movie.spanish_name = response.xpath("//dt[contains(text(), '%s')]/following-sibling::dd[1]/ul/li[1]/text()" % u'AKA').get()

		movie.year = response.css('.movie-info dd[itemprop="datePublished"]::text').get().strip()
		movie.duration = response.css('.movie-info dd[itemprop="duration"]::text').get().strip() if response.css('.movie-info dd[itemprop="duration"]::text').get() else False
		movie.country  = response.css('.movie-info dd #country-img img::attr(title)').get().strip()

		movie.images = dict()
		if response.css('[itemprop="image"]::attr(src)').get():
			movie.images = dict(
					small=response.css('[itemprop="image"]::attr(src)').get().strip().replace("mmed", "small"),
					medium=response.css('[itemprop="image"]::attr(src)').get().strip(),
					large=response.css('[itemprop="image"]::attr(src)').get().strip().replace("mmed", "large")
				)

		directors = []
		for director_p in response.css('.movie-info dd.directors').css("span[itemprop='director'] a[itemprop='url']"):
			directors.append(dict(
					name=unidecode(director_p.css('::attr(title)').get()),
					url="%s%s" % (self.url, director_p.css('::attr(href)').get())
				))
		movie.directors = directors

		guionists = []
		for guionist_p in response.xpath("//dt[contains(text(), '%s')]/following-sibling::dd[1]/div/span/span/text()" % u'Guion'):
			guionists.append(unidecode(guionist_p.get()))		
		movie.guionists = guionists

		musicians = []
		for node_m_p in response.xpath("//dt[contains(text(), '%s')]/following-sibling::dd[1]/div/span/span/text()" % u'Música'):
			musicians.append(unidecode(node_m_p.get()))
		movie.musicians = musicians

		photography = []
		for node_m_p in response.xpath("//dt[contains(text(), '%s')]/following-sibling::dd[1]/div/span/span/text()" % u'Fotografía'):
			photography.append(unidecode(node_m_p.get()))
		movie.photography = photography

		actors = []
		for actor_p in response.css('.movie-info dd').css("span[itemprop='actor'] a[itemprop='url']"):
			actors.append(dict(					
					name=unidecode(actor_p.css("span[itemprop='name']::text").get()),
					url="%s%s" % (self.url, actor_p.css('::attr(href)').get())
				))
		movie.actors = actors

		producer_ = response.xpath("//dt[contains(text(), '%s')]/following-sibling::dd[1]/div/span/span/text()" % u'Productora').get()		
		if producer_:
			if '/' in producer_:
				producer = []
				for produc in producer_.split('/'):
					producer.append(unidecode(produc.strip()))
			else:
				producer = [unidecode(producer_.strip())]
		
			movie.producer = producer
		else:
			movie.producer = []

		genres = []
		for genre_p in response.css('.movie-info dd').css('[itemprop="genre"] a'):
			genres.append(dict(					
					name=unidecode(genre_p.css('::text').get()),
					url=genre_p.css('::attr(href)').get()
				))
		movie.genres = genres

		movie.summary = response.css('.movie-info dd[itemprop="description"]::text').get().replace('(FILMAFFINITY)', "").strip()
		
		awards = [] 
		for award_p in response.css('.movie-info dd.award').css('.margin-bottom'):
			awards.append(dict(					
					name=unidecode(re.search('</a>:(.*)</div>', award_p.extract()).group(1).strip()),
					year=award_p.css('a::text').get(),
					url=award_p.css('a::attr(href)').get()
				))
		movie.awards = awards

		yield scrapy.Request('{0}{1}'.format(self.url_reviews, movie.id), callback=self.parse_reviews, meta={'movie': movie.todict()})

	def parse_reviews(self, response):
		movie = response.meta.get('movie')

		critics = []
		for n_critic in response.css('.pro-reviews table tbody tr'):
			critics.append(dict(
					author=unidecode(n_critic.css('.author div::text').get()) if n_critic.css('.author div::text').get() else '',
					media=unidecode(n_critic.css('.author em::text').get()),
					country=unidecode(n_critic.css('.c span::text').get()),
					url=n_critic.css('.text a::attr(href)').get(),
					text=unidecode(n_critic.css('.text a::text').get().replace("\"", '')) if n_critic.css('.text a::text').get() else '',
					status=n_critic.css('.c:last-child span::text').get(),
					gender=n_critic.css('.gender span::text').get(),
				))

		movie.update({'critics': critics})

		yield scrapy.Request('{0}{1}'.format(self.url_trailers, movie['id']), callback=self.parse_trailers, meta={'movie': movie})

	def parse_trailers(self, response):
		movie = response.meta.get('movie')

		trailers = []
		for n_trailer in response.css('#mt-content-cell iframe'):
			if n_trailer.css('::attr(src)').get():
				trailers.append(n_trailer.css('::attr(src)').get().strip())

		movie.update({'trailers': trailers})

		yield scrapy.Request('{0}{1}'.format(self.url_images, movie['id']), callback=self.parse_images, meta={'movie': movie})		

	def parse_images(self, response):
		movie = response.meta.get('movie')

		images = {}

		posters = []
		for n_poster in response.css('#type_imgs_2 div.colorbox-image a'):
			posters.append(n_poster.css('a::attr(href)').get())
		images['posters'] = posters

		frames = []
		for n_frame in response.css('#type_imgs_9 div.colorbox-image a'):
			frames.append(n_frame.css('a::attr(href)').get())
		images['frames'] = frames

		promo = []
		for n_promo in response.css('#type_imgs_8 div.colorbox-image a'):
			promo.append(n_promo.css('a::attr(href)').get())
		images['promo'] = promo

		wallpapers = []
		for n_wp in response.css('#type_imgs_3 div.colorbox-image a'):
			wallpapers.append(n_wp.css('a::attr(href)').get())
		images['wallpapers'] = wallpapers

		bluray = []
		for n_br in response.css('#type_imgs_7 div.colorbox-image a'):
			bluray.append(n_br.css('a::attr(href)').get())
		images['bluray'] = bluray

		dvd = []
		for n_dvd in response.css('#type_imgs_5 div.colorbox-image a'):
			dvd.append(n_dvd.css('a::attr(href)').get())
		images['dvd'] = dvd

		vhs = []
		for n_vhs in response.css('#type_imgs_6 div.colorbox-image a'):
			vhs.append(n_vhs.css('a::attr(href)').get())
		images['vhs'] = vhs

		events = []
		for n_events in response.css('#type_imgs_11 div.colorbox-image a'):
			events.append(n_events.css('a::attr(href)').get())
		images['events'] = events

		bso = []
		for n_bso in response.css('#type_imgs_12 div.colorbox-image a'):
			bso.append(n_bso.css('a::attr(href)').get())
		images['bso'] = bso

		making_of = []
		for n_mak_of in response.css('#type_imgs_13 div.colorbox-image a'):
			making_of.append(n_mak_of.css('a::attr(href)').get())
		images['making_of'] = making_of

		others = []
		for n_others in response.css('#type_imgs_14 div.colorbox-image a'):
			others.append(n_others.css('a::attr(href)').get())
		images['others'] = others

		movie.update({'images': images})

		yield movie