from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^$', views.index,name='index'),
url(r'^letsChat$', views.letsChat,name='letsChat'),
url(r'^trainChatBot/', views.trainChatBot,name='trainChatBot'),
]