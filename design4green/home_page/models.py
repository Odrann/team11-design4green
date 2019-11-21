# HOME PAGE MODELS

from django.db import models

import datetime

class Habitant(models.Model):
    h_nom = models.CharField(max_length=100, blank=False, default='somevalue')
    h_prenom = models.CharField(max_length=100, blank=False, default='somevalue')

    def __str__(self):
        return self.hab_name

class Utilisateur(models.Model):
    u_id = models.CharField(max_length=100, blank=False, default='somevalue')
    u_mdp = models.CharField(max_length=100, blank=False, default='123456')
    u_type = models.CharField(max_length=1, blank=False, default='U')
    #FK Habitant
    u_hablink = models.ManyToManyField(Habitant)

    def __str__(self):
        return self.uti_name

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
        return self.log_name

class Consommation(models.Model):
    c_date = models.DateField(default=datetime.date.today)
    c_cons = models.CharField(max_length=100, blank=False, default='somevalue')

    # Link vers longement
    c_loglink = models.ManyToManyField(Logement)

    def __srt__(self):
        return self.cons_name


class Proprietaire(models.Model):
    p_nom = models.CharField(max_length=50, blank=True, null=True, default='')
    p_pre = models.CharField(max_length=50, blank=True, null=True, default='')
    p_soc = models.CharField(max_length=50, blank=True, null=True, default='')

    #link vers loc
    p_loclink = models.ManyToManyField(Logement)






