"""music URL Configuration.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from music_app import views, api

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.tracks, name='home'),
    url(r'^tracks/(?P<id>\d+)/$', views.t_detail, name='t_detail'),
    url(r'^genres/$', views.generes, name='genres'),
    url(r'^genres/(?P<id>\d+)/$', views.g_detail, name='g_detail'),

    url(r'^tracks/$', views.search_tracks, name='search_tracks'),
    url(r'^genres/search/$', views.search_genere, name='search_genres'),

    url(r'^v1/tracks/$', api.all_tracks, name='all_tracks'),
    url(r'^v1/tracks/(?P<id>\d+)/$', api.track_detail, name='track_detail'),
    url(r'^v1/tracks$', api.search_api, name='search'),

    url(r'^v1/genres/$', api.all_generes, name='all_generes'),
    url(r'^v1/genres/(?P<id>\d+)/$', api.genere_detail, name='genere_detail'),
    url(r'^users/', include('users.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
