#URL home_page
# ------ V2 -- a_project -- VIEWS ------ #

from django.urls import path
from django.conf.urls import url

from . import views

app_name = "homePage"

urlpatterns = [
        #index for the home page
        url(r'^$', views.index, name='index'),
        url(r'^test/$', views.newtest, name='test'),
    ]
