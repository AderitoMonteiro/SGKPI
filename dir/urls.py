from django.urls import path

from .views import list_home,mudar_balanço

urlpatterns = [     
     path('list_home/', list_home, name='list_home'),
     path('mudar_balanco/', mudar_balanço, name='mudar_balanço'),
]


