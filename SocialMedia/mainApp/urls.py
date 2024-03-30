from django.urls import path 

from . import views 

app_name = 'mainApp'

urlpatterns =[
    path('',views.index,name='index'),
    path('twits/',views.HashTagShow,name='twits'),
    path('new_tweet/',views.new_tweet,name='new_tweet')
]


