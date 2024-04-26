from django.urls import path
from .views import index,how,about

urlpatterns = [

path('',index,name="index-page"),
path('about/',about,name= "about-page"),
path('how/',how,name= "how-page"),
]