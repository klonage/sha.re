from django.conf.urls import patterns, url

from sha_events import views

urlpatterns = patterns('',
    url(r'^added/', views.just_added_event, name='just_added_event'),
    url(r'^new/', views.new_event, name='new_event')
)