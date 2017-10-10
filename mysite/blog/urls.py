
from django.conf.urls import url, include

from blog import views

urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^details/(?P<article_id>\d+)$', views.article_page,name='article_page'),
    url(r'^edit/(?P<article_id>\d+)$', views.edit_page,name='edit_page'),
    url(r'^add$', views.add),
]
