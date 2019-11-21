# HOME PAGE URL

from django.urls import path
from django.conf.urls import url

from . import views

app_name = "homePage"

urlpatterns = [
        # Login page
        url(r'^$', views.index, name='index'),
        # User details views
        url(r'^(?P<user_id>[0-9]+)/$', views.user_details, name='u_details'),

        # About
        # Help
        # Logout

        # TESTS
        url(r'^consommation/$', views.conso, name='conso'),
        #Pass forget
        url(r'^(?P<user_id>[0-9]+)/consommation/$', views.conso, name='conso'),

        url(r'^recovery/$', views.pass_forget, name='pass_forget'),
        url(r'^recovery(?P<mail>.+)/$', views.pass_forget2, name='pass_forget2'),
    ]
