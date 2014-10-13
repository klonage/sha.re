from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

urlpatterns = patterns('',
                       url('', include('social_auth.urls')),
                       url('', include('django.contrib.auth.urls', namespace='auth')),
                       url(r'^auth/', include('sha_auth.urls')),
                       url(r'^event/', include('sha_events.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', include('sha_main.urls')),
                       url(r'^messages/', include('django_messages.urls')),
                       url(r'^friends/', include('friends.urls')),
                       url(r'^user/', include('sha_user.urls')),
)
