# HOME PAGE VIEWS

from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.http import Http404
from django.http import HttpResponse
from .models import Utilisateur as user
from django.conf import settings

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
    mail = request.GET.get('mail')

    if mail != '' and mail is not None:

        send_mail('subject', 'msg', 'design4green.test@gmail.com', ['odran30@gmail.com'], fail_silently=False,)

        return render(request, 'recovery/recovery.html', {'mail': mail})
    else:
        return render(request, 'recovery/recovery.html')
