from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^character$', views.character, name='character'),
    url(r'^$', views.index, name='index'),
]