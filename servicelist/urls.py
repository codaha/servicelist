from django.conf.urls import url, include

from . import views
from django.contrib import admin

urlpatterns = [
    url(r'^$', views.services, name='index'),
    url(r'^loggin/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^accounts/', include('registration.backends.default.urls')),
]