from django.conf.urls import patterns, url
from rango import views
urlpatterns = patterns('', 
                url(r'^$', views.index),
                url(r'^about/', views.about),
)