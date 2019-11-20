# HOME PAGE URL

from django.urls import path
from django.conf.urls import url

from . import views

app_name = "homePage"

urlpatterns = [
        #index for the home page
        url(r'^$', views.index, name='index'),
        # User details views
        url(r'^(?P<user_id>[0-9]+)/$', views.user_details, name='u_details'),

        # TESTS
        url(r'^consommation/$', views.conso, name='conso'),
    ]
