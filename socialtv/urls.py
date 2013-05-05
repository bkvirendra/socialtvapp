from django.conf.urls import patterns, include, url
from main import views 

from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

	url(r'^$', 'main.views.index', name='index'),

	url(r'^authenticate/$', 'main.views.authentication', name='authentication'),

	url(r'^home/$', 'main.views.home', name='homepage'),

    url(r'^about-us/$', 'main.views.about', name='about'),

    url(r'^love/$', 'main.views.love', name='love'),

    url(r'^similar_shows/$', 'main.views.similar_shows', name='similar_shows'),

    url(r'^trending/$', 'main.views.trending', name='trending'),

    url(r'^favorites/$', 'main.views.favorites', name='favorites'),

    url(r'^show/(?P<page_alias>.+?)/$', 'main.views.tv_shows_handler', name='tv_show'),

    url(r'^torrentz/$', 'main.views.torrentz', name='torrentz'),    

    url(r'^genre/$', 'main.views.genre', name='tv_show'),

    url(r'^genre/(?P<alias>.+?)/$', 'main.views.genre', name='tv_show'),

    url(r'^search/$', 'main.views.search', name='search'),

    url(r'^logout/$', 'main.views.logout_page', name='logout'),

    (r'^robots\.txt$', direct_to_template, {'template': 'robots.txt', 'mimetype': 'text/plain'}),

    # Examples:
    # url(r'^$', 'socialtv.views.home', name='home'),
    # url(r'^socialtv/', include('socialtv.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'static'}),
)