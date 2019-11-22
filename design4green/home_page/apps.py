# HOME PAGE APPS
from django.apps import AppConfig
from django.contrib import admin
from .models import Habitant, Utilisateur, Logement, Consommation, Proprietaire

admin.site.register(Habitant, Utilisateur, Logement, Consommation, Proprietaire)
class HomePageConfig(AppConfig):
    name = 'home_page'
