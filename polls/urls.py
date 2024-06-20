from django.contrib import admin
from django.urls import path,include
from polls.views import home,create,vote,result
urlpatterns = [
    path('',home,name="home"),
    path('create/',create,name="create"),
    path('result/<poll_id>',result,name="result"),
    path('vote/<poll_id>',vote,name="vote")
]
