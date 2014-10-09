from django.conf.urls import patterns, url

from sha_auth import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)