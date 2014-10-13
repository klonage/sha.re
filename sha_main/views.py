from django.shortcuts import render_to_response
from django.template.context import RequestContext
from sha_events.models import Event
from friends.models import FriendshipManager
from django.contrib.auth.models import User


def nearest_events(cnt):
    return Event.objects.order_by('start_date')[:cnt]


def index(request):
    context = RequestContext(request,
                             {'request': request,
                              'user': request.user,
                              'nearest_events': nearest_events(10)})
    mgr = FriendshipManager()
    return render_to_response('sha_main/index.html',
                              {'friends': User.objects.filter(id__in=mgr.friends_of(request.user.id))},
                              context_instance=context)
