# coding: utf-8
from django.conf.urls.defaults import patterns, url
import views

urlpatterns = patterns('',
    url(r'$', views.zipcode_view, name='brzipcode_view'),
)