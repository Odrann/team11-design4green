# HOME PAGE VIEWS

from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.http import Http404
from django.http import HttpResponse
from .models import Utilisateur as user

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

def pass_forget(request):
    print(request)
    send_mail("subject", "msg", "UnTestMail@epita.fr", ["krzysztof.dudek@epita.fr"], fail_silently=False,)
    return render(request, 'recovery/recovery.html')

def pass_forget2(request, mail):
    print(request)
    send_mail("subject", "msg", "UnTestMail@epita.fr", ["krzysztof.dudek@epita.fr"], fail_silently=False,)
    return render(request, 'index/index.html', {'mail': mail})
