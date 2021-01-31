
from django.urls import path
from . import views
from .views import listofalldata,Displaypostdata;
urlpatterns = [
		path('listofallpost/',listofalldata.as_view()),
		path('listofallpost/<slug:slug>/',Displaypostdata.as_view()),
   

]  