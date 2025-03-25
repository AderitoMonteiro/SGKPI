from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def master_view(request):
     return render(request, "master/index.html")