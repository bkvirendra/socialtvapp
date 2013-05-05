# Create your views here.
import json
import os
import re
import datetime
import ast
import requests
import logging
import random

from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login, logout as django_logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.serializers.json import DjangoJSONEncoder
from django.utils import simplejson
from django.middleware.csrf import get_token as get_csrf_token

from socialtv.settings import FACEBOOK_APP_ID, FACEBOOK_REDIRECT_URL, PERMISSIONS
from .utils import get_token, get_info, get_similar_shows
from .models import UserProfile, tv_show
from .models import love as love_model
from .recommendations import recommendations
from .torrentz import get_links as torrent_links

# basic logging config
logging.basicConfig()

## the index page
def index(request, template="home.html"):
	try:
		if request.user.is_authenticated():
			return HttpResponseRedirect("/home/")
	except Exception, e:
		logging.exception(e)
	shows_container, titles = {}, []
	genres = ['Comedy','Crime','Horror','Mystery','Romance']
	random.shuffle(genres)
	for genre in genres:
		shows_container[genre] = []
		shows_container[genre] = tv_show.objects.values('title','image_thumbnail','image_normal',\
			'regular_cast','genre','program_creator','rating').exclude(title__in=titles).filter(genre__icontains=genre).order_by('-likes')[:5]
		titles.extend([title.get('title') for title in shows_container[genre]])
	return render_to_response(template, {'x':shows_container, \
		'genres':genres, \
		'title': "Explore TV shows"}, context_instance=RequestContext(request))

def about(request, template="about_us.html"):
	if not request.user.is_authenticated():
		# if the user is not authenticated, redirect him to the Index page
		try:
			p = UserProfile.objects.get(user=request.user)
			try:
				if p.name.split(" ") > 1:
					name = p.name.split(" ")[0]
				else:
					name = p.name
			except Exception, e:
				name = p.name
				logging.exception(e)
		except Exception, e:
			name = ""
			logging.exception(e)
	else:
		name = ""
	return render_to_response(template, {'name':name}, context_instance=RequestContext(request))

def authentication(request):
	"""
		the endpoint for handling the Facebook authentication
	"""
	try:
		if request.GET.get("code"):
			just_registered = False # set the flag to false, the default
			token = get_token(request.GET.get("code"))[0] # exchange the code for token
			fetch_info = get_info(token)
			try:
				userObj = User.objects.get(username=fetch_info.get("id"))
			except User.DoesNotExist:
				#registering the user
				email = fetch_info.get("email")[:70] if (len(fetch_info.get("email")) > 70) else fetch_info.get("email")
				user = User.objects.create_user(fetch_info.get("id"), email, token)
				just_registered = True
				profile = UserProfile()
				fetch_info = get_info(token, True)
				profile.user = user
				profile.facebook_id = fetch_info.get("id")
				profile.name = fetch_info.get("name")
				profile.username = fetch_info.get("username"," ")
				profile.email = fetch_info.get("email"," ")
				profile.gender = fetch_info.get("gender")
				profile.age_range = fetch_info.get("age_range"," ")
				profile.picture = fetch_info.get("picture").get("data").get("url")
				profile.television = fetch_info.get("television")
				profile.access_token = token
				profile.save()
			# set the session variable
			if just_registered:
				auth = authenticate(username=fetch_info.get("id"), password=token)
				login(request, auth)
				return HttpResponseRedirect("/home/?getting_started=True")
			auth = authenticate(username=userObj.username, password=token)
			#auth = authenticate(username=fetch_info.get('id'), password=token)
			try:
				login(request, auth)
			except AttributeError, e:
				"""
					seems like the username and password doesnt seem to match for the user
					because either the users token has changed, because he has reauthorized the app
				"""
				logging.exception(e)
				userObj.set_password(token)
				userObj.save()
				## update the access token 
				try:
					Profile = UserProfile.objects.get(facebook_id=fetch_info.get('id'))
					Profile.access_token = token
					Profile.save()
				except Exception, e:
					raise e
				# reauthenticate the user
				auth = authenticate(username=userObj.username, password=token)
				login(request, auth)
			except Exception, e:
				logging.exception(e)
				raise e
			return HttpResponseRedirect("/home/")
	except IndexError, e:
		logging.exception(e)
		raise e
	try:
		# try checking the user is logged in
		# if yes, redirect him to the homepage
		if request.user.is_authenticated():
			return HttpResponseRedirect("/home/")
	except Exception, e:
		logging.exception(e)
		raise e
	url = "https://www.facebook.com/dialog/oauth?client_id=" + FACEBOOK_APP_ID + "&redirect_uri=" + FACEBOOK_REDIRECT_URL + "&scope=" + PERMISSIONS + "&state="
	return HttpResponseRedirect(url)

#@login_required
def home(request, template="home.html"):
	"""
		This view will handle the homepage,
		show recommendations to the user and the similar shows
	"""
	if not request.user.is_authenticated():
		# if the user is not authenticated, redirect him to the Index page
		return HttpResponseRedirect("/")
	try:
		p = UserProfile.objects.get(user=request.user)
		try:
			if p.name.split(" ") > 1:
				name = p.name.split(" ")[0]
			else:
				name = p.name
		except Exception, e:
			name = p.name
			logging.exception(e)
	except Exception, e:
		name = ""
		logging.exception(e)
	shows_container, titles = {}, []
	genres = ['Comedy','Crime','Horror','Mystery','Romance']
	random.shuffle(genres)
	for genre in genres:
		shows_container[genre] = []
		shows_container[genre] = tv_show.objects.values('title','image_thumbnail','image_normal',\
			'regular_cast','genre','program_creator','rating').exclude(title__in=titles).filter(genre__icontains=genre).order_by('-likes')[:5]
		titles.extend([title.get('title') for title in shows_container[genre]])
	return render_to_response(template, {'x':shows_container, \
		'genres':genres, \
		'name': name,\
		'title': "Explore TV shows"}, context_instance=RequestContext(request))

def torrentz(request):
	if request.GET.get("title"):
		return HttpResponse(torrent_links(request.GET.get("title")), mimetype="application/javascript")
	else:
		return HttpResponse({"error":True})

def trending(request, template="trending.html"):
	try:
		p = UserProfile.objects.get(user=request.user)
		try:
			if p.name.split(" ") > 1:
				name = p.name.split(" ")[0]
			else:
				name = p.name
		except Exception, e:
			name = p.name
			logging.exception(e)
	except Exception, e:
		name = ""
		logging.exception(e)
	try:
		shows = tv_show.objects.values('title','image_thumbnail','image_normal',\
			'regular_cast','genre','program_creator','rating').order_by('-likes').all()[:50]
	except Exception, e:
		logging.exception(e)
	return render_to_response(template, {"shows":shows, \
		'name': name, \
		'title':"Trending TV Shows"}, context_instance=RequestContext(request))

def genre(request, alias=False, template="genre.html"):
	try:
		p = UserProfile.objects.get(user=request.user)
		try:
			if p.name.split(" ") > 1:
				name = p.name.split(" ")[0]
			else:
				name = p.name
		except Exception, e:
			name = p.name
			logging.exception(e)
	except Exception, e:
		name = ""
		logging.exception(e)
	if not alias:
		return HttpResponseRedirect('/')
	genres = ['Action','Adventure','Animation','Comedy','Crime','Drama','Family',\
		'Horror','Musical','Mystery','Romance']
	if alias.lower() in (g.lower() for g in genres):
		try:
			shows = tv_show.objects.values('title','image_thumbnail','image_normal',\
			'regular_cast','genre','program_creator','rating').order_by('-likes').filter(genre__icontains=alias)[:30]
		except Exception, e:
			logging.exception(e)
		return render_to_response(template, {"shows":shows, "genre":alias.capitalize(), \
			'name': name, \
			"title":alias.capitalize() + " : Socialtv"}, context_instance=RequestContext(request))
	return HttpResponseRedirect('/home/')

def favorites(request, template="favs.html"):
	try:
		p = UserProfile.objects.get(user=request.user)
		try:
			if p.name.split(" ") > 1:
				name = p.name.split(" ")[0]
			else:
				name = p.name
		except Exception, e:
			name = p.name
			logging.exception(e)
	except Exception, e:
		name = ""
		logging.exception(e)
	try:
		data = UserProfile.objects.get(user=request.user.id)
	except Exception, e:
		raise e
	# generate the recommendations
	instance = recommendations(data)
	## fetch the recommendations
	fetch_shows = instance.get_users_shows()
	if len(fetch_shows):
		shows = fetch_shows
		random.shuffle(shows)
	not_present = True if (len(shows) == 0) else False
	slic = 40 if (len(shows) > 40) else 20
	return render_to_response(template, {"shows":shows[:slic], 
		'hide':not_present, \
		'name':name, \
		'title': 'Favorite tv shows'}, context_instance=RequestContext(request))

def tv_shows_handler(request, page_alias, template="tv_show.html"):
	"""
		this is the view that creates TV shows page
	"""
	try:
		title = " ".join(page_alias.split("-"))
	except Exception, e:
		logging.exception(e)
		return HttpResponseRedirect("/")
	try:
		show = tv_show.objects.filter(title__iexact=title).values('id','title',
			'banner','description','facebook_url','trailer_link','itunes_link',
			'amazon_link','image_thumbnail','hulu_link','showtimes','image_normal',
			'twitter','show_year','official_website','wikipedia','tvrage','tvguide','imdb',
			'netflix','topical_webpage','regular_cast','number_of_seasons','program_creator',
			'genre','currently_in_production','number_of_episodes','episode_running_time',
			'images','trailer_link','rating','number_of_seasons')[0]
		tv = tv_show.objects.get(id=show.get('id')) ## got the object
		loves = tv.loves.all().count()
		if request.user.is_authenticated():
			## allow users to love tv_shows, when they are logged in
			try:
				user = User.objects.get(id=request.user.id)
			except Exception, e:
				raise e
			try:
				user_loved = tv.loves.filter(user=user)[0]
				is_loved = True if user_loved else False
			except IndexError:
				is_loved = False
		else:
			# if not logged in, the user cannot love a tv show
			is_loved = False
	except IndexError, e:
		raise e
		#return HttpResponseNotFound()
	try:
		## check if all the 3 links exist, if they do disqualify one of them
		if show.get('amazon_link') != "-" and show.get('itunes_link') != "-" and show.get('hulu_link') != "-":
			show['amazon_link'] = "-"
	except Exception, e:
		logging.exception(e)
	try:
		cast = ', '.join(eval(show.get('regular_cast'))[:2])
	except Exception, e:
		cast = ""
		logging.exception(e)
	try:
		genre = ', '.join(eval(show.get('genre'))[:4])
	except Exception, e:
		genre = ""
		logging.exception(e)
	try:
		description = show.get('description')[:1000]
	except Exception, e:
		genre = ""
		logging.exception(e)
	try:
		rating = eval(show.get('rating'))[0]
		print rating
	except Exception, e:
		rating = 0
		logging.exception(e)
	if request.user.is_authenticated():
		try:
			p = UserProfile.objects.get(user=request.user)
			try:
				if p.name.split(" ") > 1:
					name = p.name.split(" ")[0]
				else:
					name = p.name
			except Exception, e:
				name = p.name
				logging.exception(e)
		except Exception, e:
			name = ""
			logging.exception(e)
	else:
		name = ""
	return render_to_response(template, {'show':show, \
		'cast':cast, \
		'genre':genre, \
		'loves':loves, \
		'is_loved': is_loved, \
		'rating': rating, \
		'csrf': get_csrf_token(request), \
		'name': name, \
		'title': show.get('title'), \
		'genre_complete': ', '.join(eval(show.get('genre'))), \
		'description':description}, context_instance=RequestContext(request))

def love(request):
	"""
		This view handles creating relationships between the user and the TV show
	"""
	if request.method == "POST":
		u = User.objects.get(id=request.user.id)
		show = tv_show.objects.get(id=request.POST.get('show'))
		## generate love relationship
		if not request.POST.get('delete'):
			try:
				relationship = love_model(user=u, content_object=show)
				relationship.save()
				try:
					# publish the users open graph action
					profile = UserProfile.objects.get(user=u)
					payload = {'access_token':profile.access_token, 'show':request.POST.get('url')}
					r = requests.post('https://graph.facebook.com/me/socialtv_app:love', data=payload)
					try:
						print eval(r.text)
						if eval(r.text).get('id'):
							relationship.og_id = eval(r.text).get('id')
							relationship.save()
					except Exception, e:
						logging.exception(e)
				except Exception, e:
					logging.exception(e)
			except Exception, e:
				logging.exception(e)
		## delete the love relationship
		if request.POST.get('delete'):
			user = User.objects.get(id=request.user.id)
			try:
				love_model.objects.get(object_id=request.POST.get('show'), user=user).delete()
			except Exception, e:
				logging.exception(e)
		return HttpResponse("1", mimetype="application/javascript")
		#return HttpResponse(json.dumps({"success":True}), mimetype="application/javascript")
	return HttpResponse(json.dumps({"authorized":False}), mimetype="application/javascript")

def logout_page(request):
	#check whether the true parameter exists 
	user_logout_parameter = request.GET.get('logout')
	if user_logout_parameter:
		django_logout(request) # logout the user! Destroying the session
		return HttpResponseRedirect('/')
	return HttpResponseRedirect('/')

def similar_shows(request):
	try:
		if request.GET.get('genres') and request.GET.get('show_id'):
			shows = get_similar_shows(request.GET.get('genres'), request.GET.get('show_id'))
			return HttpResponse(json.dumps(shows), mimetype="application/javascript")
	except Exception, e:
		raise e
	return HttpResponse(json.dumps({"authorized":False}), mimetype="application/javascript")

def search(request, template="search.html"):
	"""
		the instant search endpoint
	"""
	try:
		if request.GET.get('term'):
			## search the term in the DB
			pattern=re.compile("[^\w]")
			q = pattern.sub(' ', request.GET.get('term'))
			show = tv_show.objects.values('title','image_thumbnail','show_year','regular_cast','program_creator','genre').filter(title__iregex=r'^' + q + '').order_by('-likes')[:5]
			if not len(show):
				## fallback option
				show = tv_show.objects.values('title','image_thumbnail','show_year','regular_cast','program_creator','genre').filter(title__icontains=q).order_by('-likes')[:5]
		return HttpResponse(simplejson.dumps(list(show)), mimetype="application/javascript")
	except Exception, e:
		return HttpResponse(simplejson.dumps({"error":1}), mimetype="application/javascript")