from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.db import IntegrityError

from django.contrib.auth import authenticate, login


def custom_auth(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
        else:
            print("disabled account")
            # Return a 'disabled account' error message
    else:
        print("invalid login")
            # Return an 'invalid login' error message.


def index(request):
    context = RequestContext(request,
                           {'request': request,
                            'user': request.user})
    user_created = 0
    if request.method == 'POST':
        email = request.POST['InputEmail']
        username = request.POST['InputName']
        password = request.POST['InputPasswordFirst']
        second_password = request.POST['InputPasswordSecond']

        if User.objects.filter(email=email).count() > 0:
            user_created = 4

        if second_password != password:
            user_created = 3

        if user_created == 0:
            try:
                User.objects.create_user(username=username,
                                         email=email,
                                         password=password)
                user_created = 1
            except IntegrityError:
                user_created = 2

    return render_to_response('sha_auth/index.html', {"user_created": user_created},
                              context_instance=context)
