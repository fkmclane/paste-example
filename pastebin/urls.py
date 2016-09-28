from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^latest$', views.latest, name='latest'),
    url(r'^prune$', views.prune, name='prune'),
    url(r'^(?P<paste_id>[0-9]+)$', views.paste, name='paste'),
]
