from landing import views
__author__ = 'sp41mer'
from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^$', views.landing, name='index'),
]

