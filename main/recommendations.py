import logging

from .models import UserProfile, tv_show

logging.basicConfig()

class recommendations(object):
	"""docstring for recommendations"""
	def __init__(self, arg):
		#super(recommendations, self).__init__()
		self.arg = arg

	def get_users_shows(self):
		if self.arg.generated_recommendations:
			## return the processed recommendations
			return self.arg.recommendations
		## fetch the JSON television data and loop through it
		tv_shows = []
		try:
			if len(self.arg.television.get("data")) > 0:
				for each_show in self.arg.television.get("data"):
					if each_show.get("category") == "Tv show":
						try:
							show_obj = tv_show.objects.filter(title__iexact=each_show.get("name")).values('title','image_thumbnail','image_normal',\
								'regular_cast','genre','program_creator','rating')[0]
							tv_shows.append(show_obj)
						except Exception, e:
							logging.exception(e)
							pass
				## save the recommendations
				self.arg.recommendations = tv_shows
				self.arg.generated_recommendations = True
				self.arg.save()
		except Exception, e:
			logging.exception(e)
			raise e
		return self.arg.recommendations