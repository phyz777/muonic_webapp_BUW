from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from muonic_django.models import *


def index(request):
    if not request.user.is_authenticated:
        return redirect('login')

    context = {}
    template = loader.get_template('app/index.html')
    return HttpResponse(template.render(context, request))


def get_html(request):
    if not request.user.is_authenticated:
        return redirect('login')

    runs = Run.objects.all()

    context = {'user': request.user, 'runs': runs}

    # Pick out the html file name from the url. And load that template.
    load_template = request.path.split('/')[-1]
    if load_template.split('.')[-1] != 'html':
        load_template += '.html'
    template = loader.get_template('app/' + load_template)

    return HttpResponse(template.render(context, request))


def login_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('index')
    else:
        failed = not username and not password
        context = {'failed': failed}
        template = loader.get_template('app/login.html')
        return HttpResponse(template.render(context, request))


def logout_view(request):
    logout(request)
    return redirect('login')

