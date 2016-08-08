from django.conf.urls import url
from django.contrib import admin
from blog.views import *

urlpatterns = [
    url(r'^$', PageListView.as_view(), name="home"),
    url(r'^blog/', PageListView.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^post/(?P<page_id>[0-9]+)/$', page, name="page_detail"),
    url(r'^post/(?P<page_id>[0-9]+)/edit/$', edit_post, name="page_edit"),
    url(r'^new/$', new_post, name="new_post"),
    url(r'^post/(?P<page_id>[0-9]+)/delete/$', del_post, name="page_del"),

]
