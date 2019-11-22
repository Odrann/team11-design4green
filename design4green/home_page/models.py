# HOME PAGE MODELS

from django.db import models
from django import forms


import datetime

class Habitant(models.Model):
    h_nom = models.CharField(max_length=100, blank=False, default='somevalue')
    h_prenom = models.CharField(max_length=100, blank=False, default='somevalue')

    def __str__(self):
        return self.h_nom

class Utilisateur(models.Model):
    u_id = models.CharField(max_length=100, blank=False, default='somevalue')
    u_mdp = models.CharField(max_length=100, blank=False, default='123456')
    u_type = models.CharField(max_length=1, blank=False, default='U')
    #FK Habitant
    u_hablink = models.ForeignKey(Habitant, related_name="ref1", on_delete=models.CASCADE, default='NA')

    def __str__(self):
        return self.u_id

class Logement(models.Model):
    l_foyer = models.CharField(max_length=2, blank=False, default='NA')
    l_type = models.CharField(max_length=2, blank=False, default='NA')
    l_sur = models.CharField(max_length=4, blank=False, default='NA')
    l_nb_pieces = models.CharField(max_length=3, blank=False, default='NA')
    l_chauff = models.CharField(max_length=50, blank=False, default='NA')
    l_annee = models.CharField(max_length=4, blank=False, default='NA')
    l_nb_voie = models.CharField(max_length=20, blank=False, default='NA')
    l_voie = models.CharField(max_length=100, blank=False, default='NA')
    l_cp = models.CharField(max_length=10, blank=False, default='NA')
    l_ville = models.CharField(max_length=50, blank=False, default='NA')

    #FK Habok,
    l_hablink = models.ManyToManyField(Habitant)

    def __str__(self):
        return self.l_foyer

class Consommation(models.Model):
    c_date = models.CharField(max_length=10, blank=True, null=True, default='NA')
    c_cons = models.CharField(max_length=10, blank=False, default='NA')
    c_log = models.CharField(max_length=10, blank=False, default="NA")

    # Link vers longement
    c_loglink = models.ManyToManyField(Logement)

    def __srt__(self):
        return self.c_log


class Proprietaire(models.Model):
    p_nom = models.CharField(max_length=50, blank=True, null=True, default='')
    p_pre = models.CharField(max_length=50, blank=True, null=True, default='')
    p_soc = models.CharField(max_length=50, blank=True, null=True, default='')

    #link vers loc
    p_loclink = models.ManyToManyField(Logement)

    def __srt__(self):
        return self.p_nom + '|' + self.p_soc






