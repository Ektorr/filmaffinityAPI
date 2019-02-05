# -*- coding: utf-8 -*-
from flask import Flask
from flask import jsonify
import simplejson as sj
import requests


app = Flask(__name__)

#https://www.filmaffinity.com/es/search.php?stext=el+se%C3%B1or+de+los+anillos

scrapy_url = 'http://localhost:9080/crawl.json'
film_url   = 'https://www.filmaffinity.com/es/film{0}.html'
search_url = 'https://www.filmaffinity.com/es/search.php?stype=title&stext={0}'

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

@app.route("/api/by_name/<film_name>")
def film_by_name(film_name, **args):
	#try:		
	r = requests.get('{0}?spider_name=faffy_search_spider&url={1}'.format(scrapy_url, search_url.format(film_name)), headers={'Content-type': 'application/json; charset=utf-8'})
	content = sj.loads(r._content)

	if content['status'] == 'ok':
		return jsonify({'status': True, 'content': content['items']})
		#return self.film_by_id(content['items']['movies'][0])

	return jsonify({'status':False})
	#except Exception, e:
	#	print(e)
	#	return jsonify({'status':False})