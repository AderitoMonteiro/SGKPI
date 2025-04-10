from django.urls import path

from .views import list_home,mudar_balanço,balanco_g,list_balanco_geral,ver_balanco_geral,edit_balanço_geral,bloquear_balanco

urlpatterns = [     
     path('list_home/', list_home, name='list_home'),
     path('mudar_balanco/', mudar_balanço, name='mudar_balanço'),
     path('balanco_geral/', balanco_g, name='balanco_geral'),
     path('balanco_list/', list_balanco_geral, name='balanco_geral'),
     path('balanco_g_see/', ver_balanco_geral, name='balanco_g_see'),
     path('edit_balanço_geral/', edit_balanço_geral, name='edit_balanço_geral'),
     path('bloquear_balanco/', bloquear_balanco, name='bloquear_balanço'),

]


