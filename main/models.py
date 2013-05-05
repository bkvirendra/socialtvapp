from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from jsonfield import JSONField
# the models

class love(models.Model):
	user = models.ForeignKey(User)
	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	og_id = models.CharField(max_length=20, blank=True)
	content_object = generic.GenericForeignKey('content_type', 'object_id')

	def __unicode__(self):
		return str(self.object_id)

class hate(models.Model):
	user = models.ForeignKey(User)
	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = generic.GenericForeignKey('content_type', 'object_id')

	def __unicode__(self):
		return str(self.object_id)

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	facebook_id = models.CharField(max_length=20)
	name = models.CharField(max_length=100, blank=True)
	username = models.CharField(max_length=50, blank=True)
	email = models.CharField(max_length=200,  blank=True)
	gender = models.CharField(max_length=10, blank=True)
	age_range = JSONField(blank=True)
	picture =  models.CharField(max_length=199, blank=True)
	television = JSONField(blank=True)
	access_token = models.CharField(max_length=400, blank=True, null=True)
	subscriptions_count = models.IntegerField(blank=True, null=True)
	timestamp_added = models.DateTimeField(auto_now_add=True)
	generated_recommendations = models.BooleanField()
	recommendations = JSONField(blank=True)
	friends_recommendations = JSONField(blank=True)
	loves = generic.GenericRelation(love)
	hates = generic.GenericRelation(hate)

	def __unicode__(self):
		return str(self.id)

class temp_imdb_dump(models.Model):
	imdb_id = models.CharField(max_length=50)
	html_page = models.TextField(blank=True)

	def __unicode__(self):
		return str(self.id)

class tv_show(models.Model):
	gid = models.CharField(max_length=200, blank=True, default="", null=True)
	title = models.CharField(max_length=200, blank=True, default="", null=True, db_index=True)
	banner = models.CharField(max_length=500, blank=True, default="", null=True)
	status = models.CharField(max_length=50, blank=True, default="", null=True)
	description = models.TextField(blank=True, default="", null=True)
	netflix_link = models.CharField(max_length=200, blank=True, default="", null=True)
	facebook_url = models.CharField(max_length=200, blank=True, default="", null=True)
	starring = JSONField(blank=True, default="", null=True)
	image_banner = models.CharField(max_length=200, blank=True, default="", null=True)
	url = models.CharField(max_length=200, blank=True, default="", null=True)
	guru = JSONField(blank=True, default="", null=True)
	summary = models.TextField(blank=True, default="", null=True)
	trailer_link = models.CharField(max_length=200, blank=True, default="", null=True)
	itunes_link = models.CharField(max_length=200, blank=True, default="", null=True)
	amazon_link = models.CharField(max_length=500, blank=True, default="", null=True)
	image_thumbnail = models.CharField(max_length=200, blank=True, default="", null=True)
	hulu_link = models.CharField(max_length=200, blank=True, default="", null=True)
	showtimes = models.CharField(max_length=200, blank=True, default="", null=True)
	image_normal = models.CharField(max_length=200, blank=True, default="", null=True)
	images = JSONField(blank=True, default="", null=True)
	image_iphone = models.CharField(max_length=200, blank=True, default="", null=True)
	reviewed = models.IntegerField(null=True, default=0)
	likes = models.IntegerField(null=True, default=0)
	dislikes = models.IntegerField(null=True, default=0)
	image_square = models.CharField(max_length=200, blank=True, default="", null=True)
	twitter = models.CharField(max_length=200, blank=True, default="", null=True)
	show_year = models.IntegerField(default=0, null=True)
	image_wide = models.CharField(max_length=200, blank=True, default="", null=True)
	freebase_api_response = JSONField(blank=True, default="", null=True)
	official_website = models.URLField(max_length=200, blank=True, default="", null=True)
	wikipedia = models.URLField(max_length=200, blank=True, default="", null=True)
	tvrage = models.URLField(max_length=200, blank=True, default="", null=True)
	tvguide = models.URLField(max_length=200, blank=True, default="", null=True)
	imdb = models.URLField(max_length=200, blank=True, default="", null=True)
	netflix = models.URLField(max_length=200, blank=True, default="", null=True)
	topical_webpage = models.URLField(max_length=200, blank=True, default="", null=True)
	regular_cast = JSONField(blank=True, default="", null=True)
	number_of_seasons = models.IntegerField(default=0, null=True)
	program_creator = models.CharField(max_length=200, blank=True, default="", null=True)
	genre = JSONField(blank=True, default="", null=True)
	currently_in_production = models.BooleanField()
	number_of_episodes = models.IntegerField(default=0, null=True)
	episode_running_time = models.IntegerField(default=0, null=True)
	imdb_id = models.CharField(max_length=50, blank=True, default="", null=True)
	rating = models.CharField(max_length=10, blank=True, default="", null=True)
	loves = generic.GenericRelation(love)
	hates = generic.GenericRelation(hate)

	def __unicode__(self):
		return str(self.id)