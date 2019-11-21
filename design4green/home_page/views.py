# HOME PAGE VIEWS

from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.http import Http404
from django.http import HttpResponse
from .models import Utilisateur as user
from .models import Habitant
from .models import Logement
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

    try:
        h_name = Habitant.objects.get(id=user_id)
    except Habitant.DoesNotExist:
        raise Http404("Aucun habitant")


    try:
        uloc = Logement.object.get(id=h_name.id)
    except Logement.DoesNotExist:
        raise Http404("Aucun Logement")

    return render(request, 'details/user_details.html', {'user': user, 'h_name' : h_name, 'uloc': uloc})

def about(request):
    return render(request, "about/about.html")

def help(request):
    return render(request, "help/help.html")


def conso(request, user_id):
    user = get_object_or_404(Utilisateur, pk=user_id)

    return render(request, 'index/consommation.html', {'user': user})

def pass_forget(request):
    mail = request.GET.get('mail')

    if mail != '' and mail is not None:
        qs = user.objects.all()
        qs = qs.filter(u_id=mail)

        stringLength = 8
        lettersAndDigits = string.ascii_letters + string.digits
        newpass = ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

        if len(qs) == 1:
            mail = qs[0]

            currentuser = user.objects.get(u_id=mail)
            currentuser.u_mdp = newpass
            currentuser.save()
        else:
            mail = ''

        print('_____New pass: ' + newpass + ' for: ' + mail)

        send_mail('Mot de passe oublie', 'Votre nouveau mot de passe: ' + newpass, 'design4green.test@gmail.com', [mail], fail_silently=False,)

        return render(request, 'recovery/recovery.html', {'mail': mail})
    else:
        return render(request, 'recovery/recovery.html')
