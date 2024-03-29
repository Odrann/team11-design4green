# HOME PAGE VIEWS

from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.http import Http404
from django.http import HttpResponse
from .models import Utilisateur as user
from .models import Habitant
from .models import Logement
from .models import Consommation
from django.conf import settings

import json
import random
import string

# MODEMS IMPORTS
from .models import Utilisateur

def index(request):
    usr = request.POST.get('user')
    mdp = request.POST.get('mdp')

    if (usr != '' and usr is not None) or (mdp != '' and mdp is not None):
        try:
            searchuser = Utilisateur.objects.get(u_id=usr)
        except Utilisateur.DoesNotExist:
            return render(request, "index/index.html")

        print(searchuser)
        print(searchuser.id)

        if searchuser != '' and searchuser is not None:
            user = get_object_or_404(Utilisateur, pk=searchuser.id)

            try:
                h_name = Habitant.objects.get(id=searchuser.id)
            except Habitant.DoesNotExist:
                raise Http404("Aucun habitant")

            try:
                uloc = Logement.objects.get(id=h_name.id)
            except Logement.DoesNotExist:
                raise Http404("Aucun Logement")

            all_conso = Consommation.objects.all()
            all_conso = all_conso.filter(c_log=searchuser.id).order_by('id')[:5]

            return render(request, "details/user_details.html", {'user': user, 'h_name' : h_name, 'uloc': uloc, 'all_conso': all_conso})
        else:
            return render(request, "index/index.html")
    else:
        return render(request, "index/index.html")

def user_details(request, user_id):
    # try catch on one line
    user = get_object_or_404(Utilisateur, pk=user_id)

    try:
        h_name = Habitant.objects.get(id=user_id)
    except Habitant.DoesNotExist:
        raise Http404("Aucun habitant")

    try:
        uloc = Logement.objects.get(id=h_name.id)
    except Logement.DoesNotExist:
        raise Http404("Aucun Logement")

    all_conso = Consommation.objects.all()
    all_conso = all_conso.filter(c_log=user_id).order_by('id')[:5]

    return render(request, 'details/user_details.html', {'user': user, 'h_name' : h_name, 'uloc': uloc, 'all_conso': all_conso})

def about(request, user_id):
    user = get_object_or_404(Utilisateur, pk=user_id)
    return render(request, "about/about.html", {'user': user})

def help(request, user_id):
    user = get_object_or_404(Utilisateur, pk=user_id)
    return render(request, "help/help.html", {'user': user})


def conso(request, user_id):
    # try catch on one line
    user = get_object_or_404(Utilisateur, pk=user_id)

    try:
        h_name = Habitant.objects.get(id=user_id)
    except Habitant.DoesNotExist:
        raise Http404("Aucun habitant")

    try:
        uloc = Logement.objects.get(id=h_name.id)
    except Logement.DoesNotExist:
        raise Http404("Aucun Logement")

    all_conso = Consommation.objects.all()
    all_conso = all_conso.filter(c_log=user_id).order_by('id')[:14]

    listDate = []
    listConso = []

    for item in all_conso:
        listDate.append(item.c_date)
        listConso.append(item.c_cons)


    listConso = list(map(int, listConso))

    return render(request, 'index/consommation.html', {'user': user, 'h_name' : h_name, 'uloc': uloc, 'listDate': listDate, 'listConso': listConso})

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

        mail = str(mail)

        send_mail('Mot de passe oublie', 'Votre nouveau mot de passe: ' + newpass, 'design4green.test@gmail.com', [mail], fail_silently=False,)

        return render(request, 'recovery/recovery.html', {'mail': mail})
    else:
        return render(request, 'recovery/recovery.html')
