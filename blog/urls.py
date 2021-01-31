from django.urls import path
from . import views 

from .views import (Topnews,Scifi,Topwebseries,Galaxies,BigBang,WhirlpoolGalaxies,Universe )   

urlpatterns = [
	
   path('',views.home,name=''),
   path('Topnews/',Topnews.as_view()),
   path('Scifi/',Scifi.as_view()),
   path('Topwebseries/',Topwebseries.as_view()),
   path('Universe/',Universe.as_view()),
   path('Galaxies/',Galaxies.as_view()),
   path('Big_Bang/',BigBang.as_view()),
   path('WhirlpoolGalaxies/',WhirlpoolGalaxies.as_view()),
   path('Search',views.Search,name='Saerch')


] 
