from flask import Flask
import requests

app = Flask(__name__)

scrapy_url = 'http://localhost:9000/crawl.json'

@app.route("/api/<film_id>/")
def film_by_id(film_id):
	url = 'https://www.filmaffinity.com/es/film{0}.html'.format(film_id)
	r = requests.post(scrapy_url, data={'spider_name': 'filmdataspider', 'url': url})
    return film_id