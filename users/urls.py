from django.conf.urls import url
from . import views

#urlpatterns 是被django自动识别的路由列表变量
urlpatterns = [
    #每个路由信息都需要使用url函数来构造
    #url (路径正则,视图函数)
    url(r'^index/$',views.index),

    #路由匹配顺序
    url(r'^say/$',views.say),
    url(r'^sayhello/$',views.say_hello),
]
