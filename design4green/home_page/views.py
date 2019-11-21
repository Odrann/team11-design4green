# HOME PAGE VIEWS

from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponse

# MODEMS IMPORTS
from .models import Utilisateur

def index(request):
    return render(request, "index/index.html")

def user_details(request, user_id):
    # try catch on one line
    user = get_object_or_404(Utilisateur, pk=user_id)

    return render(request, 'details/user_details.html', {'user': user})






def conso(request, user_id):
    user = get_object_or_404(Utilisateur, pk=user_id)

    return render(request, 'index/consommation.html', {'user': user})
