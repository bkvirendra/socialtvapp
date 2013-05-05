import requests
import simplejson as json
import xmltodict


def get_100_shows():
	url = "http://api.getglue.com/v2/glue/popular?oauth_consumer_key=cbe1ee277ab21864ea171c1c5400917c&category=tv_shows"
	response = requests.get(url)
	o = xmltodict.parse(response.text)
	js = eval(json.dumps(o))
	for e in js["adaptiveblue"]:
		print eval(e)
