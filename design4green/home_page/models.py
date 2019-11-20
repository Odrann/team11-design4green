# HOME PAGE MODELS
from datetime import datetime

from django.db import models
from django.forms import forms


class Consommation(models.Model):
    c_loc = models.CharField(max_length=100)
    c_date = models.DateField(default=datetime.date.today)
    c_cons = models.CharField(max_length=100)

    def __srt__(self):
        return self.cons_name

class Habitant(models.Model):
    h_nom = models.CharField(max_length=100)
    h_prenom = models.CharField(max_length=100)

    def __str__(self):
        return self.hab_name

class Logement(models.Model):
    l_name = models.CharField(max_length=100)
    l_adresse = models.CharField(max_length=100)
    l_pays = models.CharField(max_length=100)
    l_ville = models.Charfield(max_length=100)
    l_cp = models.CharField(max_length=20)

    #FK Habok,
    #l_hablink = models.ManyToManyField(Habitant)

    def __str__(self):
        return self.log_name


class Utilisateur(models.Model):
    u_id = models.CharField(max_length=100)
    u_mdp = forms.CharField(max_length=32, widget=forms.PasswordInput)
    u_type = models.CharField(max_length=1)

    def __str__(self):
        return self.uti_name

