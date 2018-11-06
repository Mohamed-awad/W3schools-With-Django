from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework import generics
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

class UserList(LoginRequiredMixin, generics.ListCreateAPIView):
  login_url = 'accounts:login'
  queryset = User.objects.all()
  serializer_class = UserSerializer


class UserDetail(LoginRequiredMixin, generics.RetrieveUpdateDestroyAPIView):
  login_url = 'accounts:login'
  queryset = User.objects.all()
  serializer_class = UserSerializer


class Signup(CreateView):
  form_class = UserCreationForm
  success_url = reverse_lazy('accounts:login')
  template_name = 'accounts/signup.html'


def home(request):
  return render(request, 'home.html')


def page1(request):
  return render(request, 'page1.html')


def page2(request):
  return render(request, 'page2.html')

