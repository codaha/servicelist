
	#def __str__(self):
	#	return self.title
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blogkw.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	url(r'^admin/', include(admin.site.urls)),
	#url(r'^lista/', include(blog.views.stronaglowna))

    url(r'^$', include('blog.urls')),
)
