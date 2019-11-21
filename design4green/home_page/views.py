# HOME PAGE VIEWS

from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.http import Http404
from django.http import HttpResponse
from .models import Utilisateur as user
from django.conf import settings

import random
import string

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
        qs = user.objects.all()
        qs = qs.filter(u_id=mail)

        if len(qs) == 1:
            mail = qs[0]
        else:
            mail = ''

        stringLength = 8
        lettersAndDigits = string.ascii_letters + string.digits
        newpass = ''.join(random.choice(lettersAndDigits) for i in range(stringLength))
        #send_mail('Mot de passe oublie', 'Votre nouveau mot de passe: ' + newpass, 'design4green.test@gmail.com', [mail], fail_silently=False,)

        return render(request, 'recovery/recovery.html', {'mail': mail})
    else:
        return render(request, 'recovery/recovery.html')
