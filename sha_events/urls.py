from django.conf.urls import patterns, url

from sha_events import views

urlpatterns = patterns('',
                       url(r'^added/', views.just_added_event, name='just_added_event'),
                       url(r'^new/', views.new_event, name='new_event'),
                       url(
                           r'^events_from_range/(?P<north>-*\d+\.?\d+)/(?P<south>-*\d+\.?\d+)/(?P<east>-*\d+\.?\d+)/(?P<west>-*\d+\.?\d+)/$',
                           views.events_from_range, name='events_from_range'),
                           url('^(?P<event_id>\d+)', views.event_details),
                           url('^attend/(?P<event_id>\d+)', views.attend),
                           url('^cancel/(?P<event_id>\d+)', views.cancel)
)