from django.conf.urls import patterns, url

from sha_user import views

urlpatterns = patterns('',
                       url(r'^(?P<user_id>\d+)', views.show_profile, name='show_profile'),
)