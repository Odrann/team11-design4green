from django.shortcuts import render
from .models import Project
from django.http import Http404
# VIEWS home_page.

def index(request):
    return render(request, "index/index.html")