from django.conf.urls import url
from . import views

urlpatterns=[
    #位置参数
    url(r'^weather/([a-z]+)/(\d{4})/$',views.weather),


    #关键字参数
    url(r'^weather2/(?P<city>[a-z]+)/(?P<year>\d{4})/$', views.weather2),
]