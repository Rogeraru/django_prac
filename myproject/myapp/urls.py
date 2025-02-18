from django.urls import path
from . import views
#define a list of url petterns
#使得views 跟 website對應
urlpatterns = [ 
    #path('', views.index, name='index'), #第一個參數是網頁路徑 網頁根目錄 
    path('', views.index2, name='index2'),
]