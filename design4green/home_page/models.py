# HOME PAGE MODELS

from django.db import models

class Consommation(models.Models):
    c_name = models.CharField(max_length=100)


    def __srt__(self):
        return self.cons_name


class Logement(models.Models):
    l_name = models.CharField(max_length=100)

    def __str__(self):
        return self.log_name


class Utilisateur(models.Models):
    u_name = models.CharField(max_length=100)
    def __str__(self):
        return self.uti_name

class Habitant(models.Models):
    h_name = models.CharField(max_length=100)

    def __str__(self):
        return self.hab_name