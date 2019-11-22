# HOME PAGE APPS
from django.apps import AppConfig
from django.contrib import admin
from .models import Habitant


admin.site.register(Habitant)


class HomePageConfig(AppConfig):
    name = 'home_page'


