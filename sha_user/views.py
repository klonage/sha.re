from django.shortcuts import render
from django.contrib.auth.models import User
from friends.models import FriendshipManager, FriendshipRequest
from sha_events.models import Event


def get_facebook_uid(user):
    social_user = user.social_auth.filter(provider='facebook',).first()
    if social_user:
            return social_user.uid, social_user.extra_data['access_token']
    return 0, 0


class FriendshipStatus:
    NO_FRIENDS = 1
    ARE_FRIENDS = 2
    WAIT_FOR_RESPONSE = 3
    INVITATION_SENT = 4
    CANT_BE_FRIEND = 5


def show_profile(request, user_id):
    mgr = FriendshipManager()
    user_profile = User.objects.get(id=user_id)

    invitation_status = FriendshipStatus.NO_FRIENDS

    if request.user == user_profile:
        invitation_status = FriendshipStatus.CANT_BE_FRIEND
    elif mgr.are_friends(request.user, user_profile):
        invitation_status = FriendshipStatus.ARE_FRIENDS
    elif FriendshipRequest.objects.filter(from_user_id=request.user.id, to_user_id=user_profile.id).count() > 0:
        invitation_status = FriendshipStatus.WAIT_FOR_RESPONSE
    elif FriendshipRequest.objects.filter(to_user_id=request.user.id, from_user_id=user_profile.id).count() > 0:
        invitation_status = FriendshipStatus.INVITATION_SENT

    fb_id, fb_token = get_facebook_uid(user_profile)


    return render(request,
                  'sha_user/profile.html',
        {'user_profile': user_profile,
         'invitation_status': invitation_status,
         'user_fb_id': fb_id,
         'user_events': Event.objects.all(),
         'friends': mgr.friends_of(user_profile)})