from django.shortcuts import render
from django.contrib.auth.models import User
from friends.models import FriendshipManager


def show_profile(request, user_id):
    mgr = FriendshipManager()

    user_profile = User.objects.get(id=user_id)
    return render(request,
                  'sha_user/profile.html',
        {'user_profile': user_profile,
         'friends': User.objects.filter(id__in=mgr.friends_of(user_profile.id))})