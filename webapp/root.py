# -*- coding: utf-8 -*-
from flask import Flask
from flask import jsonify
import urllib
import simplejson as sj
import requests

app = Flask(__name__)

#https://www.filmaffinity.com/es/search.php?stext=el+se%C3%B1or+de+los+anillos

scrapy_url = 'http://localhost:9080/crawl.json'
film_url   = 'https://www.filmaffinity.com/es/film{0}.html'
search_url = 'https://www.filmaffinity.com/es/search.php?stext={0}'

list_topic_url = 'https://www.filmaffinity.com/es/movietopic.php?topic={0}&attr=all&nodoc'
topic_url      = 'https://www.filmaffinity.com/es/topics.php'

@app.route("/api/<film_id>/")
def film_by_id(film_id):
	try:		
		r = requests.get('{0}?spider_name=filmdataspider&url={1}'.format(scrapy_url, film_url.format(film_id)), headers={'Content-type': 'application/json; charset=utf-8'})				
		content = sj.loads(r._content)

		if content['status'] == 'ok':
			return jsonify({'status': True, 'content': content['items']})

		return jsonify({'status':False})
	except Exception, e:
		print(e)
		return jsonify({'status':False})

@app.route("/api/name/<film_name>")
def film_by_name(film_name, **args):
	try:	
		r = requests.get('{0}?spider_name=faffy_search_spider&url={1}'.format(scrapy_url, search_url.format(urllib.quote_plus(film_name))), headers={'Content-type': 'application/json; charset=utf-8'})
		content = sj.loads(r._content)

		if content['status'] == 'ok':
			movies = content['items'][0]['movies']
			if len(movies) > 0:
				return film_by_id(movies[0])

		return jsonify({'status':False, 'msg':"No films"})
	except Exception, e:
		print(e)
		return jsonify({'status':False})

@app.route("/api/topic/")
def topics(**args):
	try:	
		# Return a list with all the topics -> https://www.filmaffinity.com/es/topics.php
		r = requests.get('{0}?spider_name=faffy_topic_spider&url={1}'.format(scrapy_url, topic_url), headers={'Content-type': 'application/json; charset=utf-8'})
		content = sj.loads(r._content)

		if content['status'] == 'ok':
			return jsonify({'status':True, 'topics': content['items'][0]})

		return jsonify({'status':False, 'msg':"No films"})
	except Exception, e:
		print(e)
		return jsonify({'status':False})

@app.route("/api/topic/<id_topic>")
@app.route("/api/topic/<id_topic>/<limit>/")
def films_by_topic(id_topic, limit='', **args):
	try:	
		# Return a list all the films from a topic -> https://www.filmaffinity.com/es/topics.php
		r = requests.post(scrapy_url,  headers={'Content-type': 'application/json; charset=utf-8'}, data=sj.dumps({"request":{"url":"{0}&limit={1}".format(list_topic_url.format(id_topic), limit)}, "spider_name": "faffy_search_spider"}))
		content = sj.loads(r._content)

		if content['status'] == 'ok':
			return jsonify({'status':True, 'topics': content['items'][0]})

		return jsonify({'status':False, 'msg':"No films"})
	except Exception, e:
		print(e)
		return jsonify({'status':False})