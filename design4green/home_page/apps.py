# HOME PAGE APPS
from django.apps import AppConfig
from django.contrib import admin
from .models import * as allmod

admin.site.register(allmod)
class HomePageConfig(AppConfig):
    name = 'home_page'
