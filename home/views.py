from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView


# Create your views here.
# Creating our First Class based View of the Home Page instead of the Former
# Functions Based Views - - - --

class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'

class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'


class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'today': datetime.today()}


class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorized.html'
    login_url = '/admin'


# All these Below are all the Endpoints created using the Functions Based Declarations.

"""def home(request):
    return render(request, 'home/welcome.html', {'today': datetime.today()})"""

"""@login_required(login_url='/admin')
def authorized(request):
    return render(request, 'home/authorized.html', {})"""
