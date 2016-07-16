"""lonesome_zeus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from blog.views import index, PageListView, page, testare # ca sa avem un view trebuie sa-l si importam!

urlpatterns = [
    url(r'^$', index),
    url(r'^blog/', PageListView.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^hello/', index),
    url(r'^page/(?P<page_id>[0-9])/$', page),
    url(r'^testare', testare),
]
