"""URL configuration for Users."""
from django.conf.urls import url
from .views import register, login, logout, account


urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^account/$', account, name='account'),
]
