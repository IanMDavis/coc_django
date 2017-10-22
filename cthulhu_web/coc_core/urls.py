from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^character$', views.character, name='character'),
    url(r'^create_user$', views.create_user, name='create_user'),
    url(r'^$', views.index, name='index'),
]