from django.conf.urls import include,url

from . import views

urlpatterns = [
   url('newaccount', views.getAccount, name='account'),
   url('accountlist', views.getAccountList, name='Account list'),
]