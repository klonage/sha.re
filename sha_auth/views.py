from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import redirect

from django.contrib.auth import authenticate, login


def custom_auth(request):
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            if not request.POST.get('remember_me', None):
                request.session.set_expiry(0)
            login(request, user)
            return 0
        else:
            return 1
    else:
        return 2


def custom_register(request):
    email = request.POST['InputEmail']
    username = request.POST['InputName']
    password = request.POST['InputPasswordFirst']
    second_password = request.POST['InputPasswordSecond']

    if User.objects.filter(email=email).count() > 0:
        return 4

    if second_password != password:
        return 3

    try:
        User.objects.create_user(username=username,
                                     email=email,
                                     password=password)
        return 1
    except IntegrityError:
        return 2


def index(request):
    context = RequestContext(request,
                             {'request': request,
                              'user': request.user})
    user_created = 0
    user_signin = 0
    if request.method == 'POST':
        if request.POST.get('signupform', 0):
            user_created = custom_register(request)
        if request.POST.get('signinform', 0):
            custom_auth(request)
            return redirect('/')

    return render_to_response('sha_auth/index.html',
                              {"user_created": user_created,
                               "user_signin": user_signin},
                              context_instance=context)
