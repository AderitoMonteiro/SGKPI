from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def login_view(request):
     return render(request, "auth/login.html")