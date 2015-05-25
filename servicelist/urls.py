

from . import views

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', views.services, name='index'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),

	url(r'^admin/', include(admin.site.urls)),
]