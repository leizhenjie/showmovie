"""movie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from app01 import views as app01_views
from django.views.static import serve
import re
from . import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^$', app01_views.music, name="music"),
    url(r'^$', app01_views.index, name='index'),
    url(r'^detail/movie_id=(\d+)', app01_views.Detail.as_view(), name='movie_detail'),
    url(r'^apis/', include('apis.urls', namespace="apis")),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^search/', app01_views.search, name="search"),
    url(r'^star/$', app01_views.star, name="star"),
    url(r'^rank_list/$', app01_views.rank_list, name='rank_list'),
    url(r'^news', app01_views.news, name="news"),

    url(r'^%s(?P<path>.*)$' % re.escape(settings.STATIC_URL.lstrip('/')), serve
        ,
        {"document_root": settings.STATIC_ROOT, }),
]
handler404 = app01_views.my404
