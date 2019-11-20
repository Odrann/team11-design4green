# HOME PAGE VIEWS

from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1> Test2 </h1>")