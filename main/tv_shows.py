import requests
import json
import urllib2
import urllib
import urlparse
import logging
import time
import lxml.html

logging.basicConfig()

from .models import tv_show, temp_imdb_dump
from django.db import connection
from django.utils.encoding import smart_str

API_KEY = "AIzaSyAdAQtiMBsm-YfTwePiGTylHFXY6g5xFcs"
cookie = 'session-id=506-2573762-0042710; session-id-time=1510253762; uu=BCYoiJtGASjn03OIBThWZtSI_jgjC-hdrcrugPm4RQSLAhSKAHybjFabhiF8z287FrUsoRo0ehxx48ygPYpPkfvoID3wlb91gJaZG2ecJRF7_aRIfhNhsPEM7qFL9phDFmE1bC7sHP_NqDWLOSkjJ6_CxK-fuAjtb2YeKriaYmOpgxm117Gqe5kctatSCxrxDjZsr7Ve1VGggE56YcwvZn5xI4piJHJJeQUrT3BkKM86NHE9uATl_Qt1fZeOwsX8m2JPrxdnGY90A-v-XcSnIRsIRJiCzNR0uXO1ztfqYJW4zu_O-UuDj_b0JvZy25mUpmKgsKE26tmyG9LtoYjQEc0BMA; ap=995%2C1972%2C4723%2C555%2C1127%2C1115%2C608%2C921; fsr.s={"v":1,"rid":"d1159f3-80516037-1b64-08c8-9f3ec","ru":"http://www.imdb.com/","r":"www.imdb.com","st":"","to":5,"c":"http://www.imdb.com/title/tt0078129/","pv":7,"lc":{"d0":{"v":7,"s":true}},"cd":0,"f":1360465974470,"cp":{"searchterms":"Quatermass,spider+man+animated"},"sd":0}; us=s%3D3072%3Bs%3D3073%3Bs%3D32%3Bs%3D863a%3Bs%3D863%3Bs%3D24b%3Bs%3D24%3Bs%3D1%3Bs%3D3%3Bs%3D9%3Bs%3D12%3Bs%3D67%3Bs%3D95%3Bs%3D130%3Bs%3D142%3Bs%3D145%3Bs%3D150%3Bs%3D153%3Bs%3D176%3Bs%3D283%3Bs%3D284%3Bs%3D315%3Bs%3D333%3Bs%3D334%3Bs%3D335%3Bs%3D336%3Bs%3D337%3Bs%3D338%3Bs%3D339%3Bs%3D340%3Bs%3D341%3Bs%3D342%3Bs%3D343%3Bs%3D344%3Bs%3D437%3Bs%3D439%3Bs%3D622%3Bs%3D833%3Bs%3D921%3Bs%3D1009%3Bs%3D1046%3Bs%3D1302%3Bs%3D1303%3Bs%3D1324%3Bs%3D2366%3Bs%3D2487%3Bs%3D2674%3Bs%3D3101%3Bs%3D3102%3Bs%3D3103%3Bs%3Dc1%3Bs%3Dc4%3Bs%3Dc4%3Bs%3Dc14%3Bs%3Dc12%3Bs%3Dc2%3B; __utma=68898382.553044785.1360467710.1360467710.1360467710.1; __utmb=68898382.0.10.1360467710; __utmc=68898382; __utmz=68898382.1360467710.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=68898382.|3=usertype=registered=1; cs=i8N4HQqD+GM1q3HUFcCTdgeBbbqgkVqM8Bt9uqOS/TNj0g7J04Je2aCRXRoA0U26oKcq7CbRbbqjlQs5t9HN2cCRWyxAGW26oKdbraCRbbqgsW26oJFt+uDBHYqg==; as=%7B%22h%22%3A%7B%22t%22%3A%5B0%2C0%5D%2C%22tr%22%3A%5B0%2C0%5D%2C%22in%22%3A%5B0%2C0%5D%2C%22ib%22%3A%5B0%2C0%5D%7D%2C%22n%22%3A%7B%22t%22%3A%5B728%2C85%5D%2C%22tr%22%3A%5B300%2C250%5D%2C%22in%22%3A%5B0%2C0%5D%2C%22ib%22%3A%5B0%2C0%5D%7D%7D; id=BCYhVT5sKUzpwJpJEzWh9oSHRWZAtDWFtUDmPQhWoa1X2IdCVCgCuH5txYAuh_rGv2ehkcVX2M8AqSKaUSp4BsfI5eOqZjlBqhaAmY27qpBwzkDb4NAiOyqteyJwV35AUITbG2lYnU7Ve4CED5mxRup6EyUxegps4xmZMjjwHE7_FLRa89ght1koyH8sxUgcLdG-'

def store_imdb_page(imdb_id):
	try:
		a = requests.get("http://www.imdb.com/title/" + imdb_id)
	except Exception, e:
		logging.exception(e)
		time.sleep(2)
		store_imdb_page(imdb_id)
	try:
		ob = temp_imdb_dump(imdb_id=imdb_id, html_page=a.content)
		ob.save()
		print imdb_id
	except Exception, e:
		logging.exception(e)
	return

def get_imdb_info(imdb_id):
	## get the html string from the temp_imdb_db
	try:
		imdb_response = temp_imdb_dump.objects.get(imdb_id=imdb_id)
	except Exception, e:
		return 0
	response = {}
	html = lxml.html.fromstring(imdb_response.html_page)
	try:
		response['rating'] = html.xpath("//*[@id='overview-top']/div[2]/div[3]/strong/span/text()")[0]
	except IndexError:
		response['rating'] = 0
	return response.get('rating',0)

def get_ratings(show):
	#key = 'CE29E7E97F214779'
	agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.69 Safari/537.17'
	url = 'http://www.imdb.com/xml/find?json=1&q=' + show.title.replace(" ","+")
	try:
		data = requests.get(url, headers={'User-Agent':agent,'Cookie':cookie})
	except Exception, e:
		logging.exception(e)
		time.sleep(2)
		get_ratings(show)
	try:
		js = eval(data.content)
		try:
			if js.get('title_exact'):
				if 'tv series' in js.get('title_exact')[0].get('title_description').lower():
					for k in js.get('title_exact'):
						show.imdb_id = k.get('id')
						show.save()
						store_imdb_page(k.get('id'))
						show.rating = get_imdb_info(k.get('id'))
						show.save()
						print show.title + " :" + show.imdb_id
						return True
			if js.get('title_popular'):
				if 'tv series' in js.get('title_popular')[0].get('title_description').lower():
					for k in js.get('title_popular'):
						show.imdb_id = k.get('id')
						show.save()
						store_imdb_page(k.get('id'))
						show.rating = get_imdb_info(k.get('id'))
						show.save()
						print show.title + " :" + show.imdb_id
						return True
		except Exception, e:
			logging.exception(e)
	except Exception, e:
		logging.exception(e)
	return

def fetch_ratings():
	for show in tv_show.objects.all():
		get_ratings(show)
	return

def get_freebase_response(id, showObj):
	# get the freebase response and store it
	response = {}
	params = {
  		'key': API_KEY
  	}
	service_url = 'https://www.googleapis.com/freebase/v1/topic'
	try:
		url = service_url + id + '?' + urllib.urlencode(params)
	except Exception, e:
		logging.exception(e)
		return
	try:
		topic = json.loads(urllib.urlopen(url).read())
	except Exception, e:
		logging.exception(e)
		pass
	for _property in topic['property']:
		if _property == "/tv/tv_program/genre":
			response['genre'] = []
			for value in topic['property'][_property]['values']:
				response['genre'].append(value['text'])
		if _property == "/common/topic/topic_equivalent_webpage":
			#response['topic_equivalent_webpage'] = []
			for value in topic['property'][_property]['values']:
				#response['topic_equivalent_webpage'].append(value['text'])
				try:
					if urlparse.urlparse(value['text']).netloc == "en.wikipedia.org":
						response['wikipedia'] = value['text']
					if urlparse.urlparse(value['text']).netloc == "www.tvrage.com":
						response['tvrage'] = value['text']
					if urlparse.urlparse(value['text']).netloc == "www.tvguide.com":
						response['tvguide'] = value['text']
					if urlparse.urlparse(value['text']).netloc == "www.imdb.com":
						response['imdb'] = value['text']
					if urlparse.urlparse(value['text']).netloc == "movi.es":
						response['netflix'] = value['text']
				except Exception, e:
					logging.exception(e)
					pass
		if _property == "/tv/tv_program/regular_cast":
			response['regular_cast'] = []
			try:
				for value in topic['property'][_property]['values']:
					for cast in value['property']['/tv/regular_tv_appearance/actor']['values']:
						response['regular_cast'].append(cast['text'])
			except Exception, e:
				logging.exception(e)
				pass
		# official website for show
		if _property == "/common/topic/official_website":
			response['official_website'] = topic['property'][_property]['values'][0]['text']
		if _property == '/common/topic/topical_webpage':
			response['topical_webpage'] = topic['property'][_property]['values'][0]['text']
		if _property == "/tv/tv_program/currently_in_production":
			response['currently_in_production'] = topic['property'][_property]['values'][0]['value']
		if _property == '/tv/tv_program/episode_running_time':
			response['episode_running_time'] = topic['property'][_property]['values'][0]['value']
		if _property == "/tv/tv_program/number_of_episodes":
			response['number_of_episodes'] = topic['property'][_property]['values'][0]['value']
		if _property == "/tv/tv_program/number_of_seasons":
			response['number_of_seasons'] = topic['property'][_property]['values'][0]['value']
		if _property == "/tv/tv_program/program_creator":
			response['program_creator'] = topic['property'][_property]['values'][0]['text']
	showObj.freebase_api_response = topic
	showObj.official_website = response.get("official_website","-")
	showObj.wikipedia = response.get("wikipedia","-")
	showObj.tvrage = response.get("tvrage", "-")
	showObj.tvguide = response.get("tvguide","-")
	showObj.imdb = response.get("imdb","-")
	showObj.netflix = response.get("netflix","-")
	showObj.topical_webpage = response.get("topical_webpage","-")
	showObj.regular_cast = response.get("regular_cast","-")
	showObj.number_of_seasons = int(response.get("number_of_seasons",0))
	showObj.program_creator = response.get("program_creator","-")
	showObj.genre = response.get("genre","-")
	try:
		if isinstance(response.get("currently_in_production"), bool):
			pass
		else:
			response['currently_in_production'] = False
	except Exception, e:
		response['currently_in_production'] = False
		logging.exception(e)
		pass
	showObj.currently_in_production = response.get("currently_in_production")
	showObj.number_of_episodes = int(response.get("number_of_episodes",0))
	showObj.episode_running_time = int(response.get("episode_running_time",0))
	showObj.save()
	return

def get_freebase_id(showObj):
	search_url = 'https://www.googleapis.com/freebase/v1/search'
	params = {
	  'key': API_KEY, 
	  'query': smart_str(showObj.title),
	  'limit': '5',
	  'type': '/tv/tv_program'
	}
	try:
		s_url = search_url + '?' + urllib.urlencode(params)
	except Exception, e:
		logging.exception(e)
		return
	try:
		results = json.loads(urllib2.urlopen(s_url).read())
	except Exception, e:
		logging.exception(e)
		pass
	for result in results.get("result"):
		if result.get('id'):
			if result.get('name') == showObj.title:
				try:
					get_freebase_response(result.get('id'), showObj)
				except Exception, e:
					connection._rollback()
					logging.exception(e)
					pass
		break
	return

def populate_freebase():
	for show in tv_show.objects.all():
		get_freebase_id(show)
		print show.id
	return

def read_shows():
	"""
		iterates over the shows.txt
	"""
	for line in open("shows.txt"):
		yield line.strip()

def get_object_key(title):
	"""
		get the object key from getglue
	"""
	url = "http://search.guide.getglue.com/objects?q=" + title + "&category=tv_shows"
	try:
		js_resp = requests.get(url)
		resp = js_resp.json()
		if len(resp):
			obj_id = resp[0].get("object_key")
		else:
			obj_id = False
	except Exception, e:
		logging.exception(e)
	return obj_id

def dump_tv_shows():
	""" 
		get the list of tv shows from the shows.txt
		and iterate over each and get the getglue response o
		and dump it in the DB
	"""
	url = "http://ws.guide.getglue.com/v4/objects/"
	print "Starting..."
	for show in read_shows():
		print "Show." + str(show)
		try:
			obj_k = get_object_key(show)
			print "Objkey :" + str(obj_k)
			try:
				if obj_k:
					print "Obj key present" + str(obj_k)
					content_url = url + obj_k
					try:
						js_show_resp = requests.get(content_url)
						print "fetched js_show response, status_code " + str(js_show_resp.status_code)
					except Exception, e:
						logging.exception(e)
						pass
					if js_show_resp.json:
						j = js_show_resp.json()
						## have the show response add in the DB
						try:
							tv = tv_show(title=j.get("title","-"), \
								gid=j.get("id","-"),\
								banner=j.get("banner","-"),\
								status=j.get("status","-"),\
								description=j.get("description","-"),\
								netflix_link=j.get("netflix_link","-"),\
								facebook_url=j.get("facebook","-"),\
								starring=j.get("starring","-"),\
								image_banner=j.get("image_banner","-"),\
								url=j.get("url","-"),\
								guru=j.get("guru","-"),\
								summary=j.get("summary","-"),\
								trailer_link=j.get("trailer_link","-"),\
								itunes_link=j.get("itunes_link","-"),\
								amazon_link=j.get("amazon_link","-"),\
								image_thumbnail=j.get("image_thumbnail","-"),\
								hulu_link=j.get("hulu_link","-"),\
								showtimes=j.get("showtimes","-"),\
								image_normal=j.get("image_normal","-"),\
								images=j.get("images","-"),\
								image_iphone=j.get("image_iphone","-"),\
								reviewed=j.get("reviewed",0),\
								likes=j.get("likes",0),\
								dislikes=j.get("dislikes",0),\
								image_square=j.get("image_square","-"),\
								twitter=j.get("twitter","-"),\
								show_year=j.get("year",0),\
								image_wide=j.get("image_wide","-"))
							tv.save()
							print vars(tv)
						except Exception, e:
							connection._rollback()
							pass
			except Exception, e:
				logging.exception(e)
				pass
		except Exception, e:
			logging.exception(e)
			pass