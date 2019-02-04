# -*- coding: utf-8 -*-
from flask import Flask
from flask import jsonify
import simplejson as sj
import requests

app = Flask(__name__)

scrapy_url = 'http://localhost:9080/crawl.json'

@app.route("/api/<film_id>/")
def film_by_id(film_id):
	try:
		url = 'https://www.filmaffinity.com/es/film{0}.html'.format(film_id)	
		r = requests.get('http://localhost:9080/crawl.json?spider_name=filmdataspider&url={0}'.format(url))
		r.encoding = 'utf-8'

		content = sj.loads(r._content.decode('utf-8'))

		if content['status'] == 'ok':
			print(content['items'])
			return jsonify({'status':True, 'content':content['items']})

		return jsonify({'status':False})
	except Exception, e:
		print(e)
		return jsonify({'status':False})