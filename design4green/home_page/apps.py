# HOME PAGE APPS
from django.apps import AppConfig
from django.contrib import admin
from .models import Habitant, Utilisateur, Logement, Consommation, Proprietaire


admin.site.register(Habitant)
admin.site.register(Utilisateur)
admin.site.register(Logement)
admin.site.register(Consommation)
admin.site.register(Proprietaire)

class HomePageConfig(AppConfig):
    name = 'home_page'


