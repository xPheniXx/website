from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='home-index'),
    url(r'^about/$', views.about, name='home-about')
]
