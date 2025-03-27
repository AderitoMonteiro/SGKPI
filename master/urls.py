from django.urls import path

from .views import master_view,create_objetivo_estrategico,list_create_objetivo_estrategico,editar_objetivo_estrategico
app_name = "master"
urlpatterns = [
   path('dashboard/', master_view, name='dashboard'),
   path('add_OE/',  create_objetivo_estrategico, name='create_OE'),
   path('list_OE/', list_create_objetivo_estrategico, name='list_OE'),
   path('editar_OE/', editar_objetivo_estrategico, name='editar_OE'),
]
