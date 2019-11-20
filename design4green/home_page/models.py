# HOME PAGE MODELS

from django.db import models

class Consommation(models.Model):
    c_name = models.CharField(max_length=100)


    def __srt__(self):
        return self.cons_name


class Logement(models.Model):
    l_name = models.CharField(max_length=100)

    def __str__(self):
        return self.log_name


class Utilisateur(models.Model):
    u_name = models.CharField(max_length=100)
    def __str__(self):
        return self.uti_name

class Habitant(models.Model):
    h_name = models.CharField(max_length=100)

    def __str__(self):
        return self.hab_name