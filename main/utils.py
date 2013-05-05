import requests
import json
import lxml.html

from urlparse import parse_qs
from socialtv.settings import FACEBOOK_APP_ID, FACEBOOK_APP_SECRET, FACEBOOK_REDIRECT_URL

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.serializers.json import DjangoJSONEncoder
from .models import tv_show
from django.db.models import Q

def get_similar_shows(genre, excluded_show_id):
	"""
		finds the similar tv shows to that particular
	"""
	common_genres = ['Action','Adventure','Animation','Comedy','Crime','Drama','Family','Horror',\
		'Musical','Mystery','Romance', 'Fiction', 'Thriller','Talk Show']
	lowered_g = [g.lower() for g in common_genres]
	genre_list = genre.lower().split(",")
	q = "results = tv_show.objects.exclude(id=excluded_show_id).values('title','image_thumbnail','image_normal',\
			'regular_cast','genre','program_creator','rating')"
	for genre in genre_list:
		if genre.strip() in lowered_g:
			st = ".filter(genre__icontains=\"" + genre.strip() + "\")"
			q = q + st
	q = q + '[:4]'
	exec(q)
	return list(results)

def get_info(token, info=False):
	url = "https://graph.facebook.com/me?fields=first_name,id,email&access_token=" + token if (not info) else "https://graph.facebook.com/me?fields=television,email,first_name,id,name,username,gender,age_range,picture&access_token=" + token
	try:
		response = requests.get(url)
	except Exception, e:
		logging.exception(e)
	return response.json

def get_token(code):
	url = "https://graph.facebook.com/oauth/access_token?client_id=" + FACEBOOK_APP_ID + \
		"&redirect_uri=" + FACEBOOK_REDIRECT_URL + \
		"&client_secret=" + FACEBOOK_APP_SECRET + "&code=" + code
	try:
		body = requests.get(url)
	except Exception, e:
		pass
	body_query = parse_qs(body.content)
	token = body_query['access_token']
	return token

def get_wiki_shows():
	try:
		data = requests.get("http://en.wikipedia.org/wiki/List_of_television_programs_by_name")
	except Exception, e:
		raise e
	html = lxml.html.fromstring(data.content)
	count = 1
	text_file = open("shows.txt", "w")
	while count < 28:
		for ge in html.xpath("//*[@id='mw-content-text']/ul["+ str(count) +"]/li/i/a/text()"):
			text_file.write(ge.encode('utf-8').strip())
			text_file.write("\n")
		count += 1
	text_file.close()
	pass