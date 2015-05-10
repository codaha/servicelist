
	#def __str__(self):
	#	return self.title
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

	url(r'^admin/', include(admin.site.urls)),
	#url(r'^lista/', include(blog.views.stronaglowna))

    url(r'^$', include('blog.urls')),

    url(r'^login/$', 'blog.views.logowanie'),

    url(r'^logout/$', 'blog.views.wyloguj'),

	url(r'^dodaj/$', 'blog.views.dodajnowy'),

	url(r'^kolejnosc/$', 'blog.views.kolejnosc'),
)
