from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.stronaglowna, name='index'),
    url(r'^login/$', views.logowanie, name='index'),
]