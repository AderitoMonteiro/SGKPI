from django.urls import path

from .views import master_view,create_objetivo_estrategico

app_name = "master"
urlpatterns = [

   path('dashboard/', master_view, name='dashboard'),
   path('add_OE/', create_objetivo_estrategico, name='create_OE'),
]