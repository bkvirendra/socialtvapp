import logging

logging.basicConfig()

from django import template
register = template.Library()

@register.filter
def get_item(dictionary, key):
	return dictionary.get(key)

@register.filter
def return_2_stars(cast, val):
	try:
		stars = eval(cast)
	except Exception, e:
		logging.exception(e)
		return "-"
	return ", ".join(stars[:2])

@register.filter
def eval_return_rating(rating_arr, val):
	try:
		return eval(rating_arr)[0]
	except Exception, e:
		logging.exception(e)
		return 0