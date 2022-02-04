from django import template
from django.contrib.auth.models import User
from django.db import models
from django.http import HttpResponse, HttpResponseRedirect, request
from django.template import Template,Context, context
from django.shortcuts import redirect, render
from django.views.generic.edit import DeleteView
from stripe.api_resources.checkout import session
from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView, RedirectView, UpdateView, TemplateView, CreateView
from django.db.models import Q, Max, Min, query
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy, reverse
import smtplib
from decouple import config
from django. contrib.auth.models import User
from django.conf import settings
from administrador.models import  Usuario

def registro(request):
     return render(request,'registrar.html')

class Registrar(CreateView):
     template_name='registrar.html'
     model=Usuario
     fields=('nombres','apellidos','email','password',)
     success_url=reverse_lazy('registrar')
    # login_url='/ingresar/'