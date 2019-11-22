from django.contrib import admin

# Register your models here.

from .models import Habitant, Utilisateur, Logement, Consommation, Proprietaire


admin.site.register(Habitant)
admin.site.register(Utilisateur)
admin.site.register(Logement)
admin.site.register(Consommation)
admin.site.register(Proprietaire)