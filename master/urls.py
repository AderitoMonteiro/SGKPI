from django.urls import path

from .views import master_view,create_objetivo_estrategico,list_create_objetivo_estrategico,editar_objetivo_estrategico,delete_objetivo_estrategico,delete_checkbox_objetivo_estrategico,list_rastreabilidade,create_rastreabilidade,editar_rastreabilidade,delete_rastreabilidade,delete_checkbox_rastreabilidade,list_meta,create_meta, delete_rastreabilidade,editar_meta,delete_meta,delete_checkbox_meta

app_name = "master"
urlpatterns = [
   path('dashboard/', master_view, name='dashboard'),
   path('add_OE/',  create_objetivo_estrategico, name='create_OE'),
   path('list_OE/', list_create_objetivo_estrategico, name='list_OE'),
   path('editar_OE/', editar_objetivo_estrategico, name='editar_OE'),
   path('delete_OE/', delete_objetivo_estrategico, name='delete_OE'),
   path('delect_checkbox_OE/', delete_checkbox_objetivo_estrategico, name='delect_checkbox_OE'),
   path('list_RAS/', list_rastreabilidade, name='list_RAS'),
   path('add_RAS/',  create_rastreabilidade, name='create_RAS'),
   path('editar_RAS/', editar_rastreabilidade, name='editar_RAS'),
   path('delete_RAS/', delete_rastreabilidade, name='delete_RAS'),
   path('delect_checkbox_RA/', delete_checkbox_rastreabilidade, name='delect_checkbox_RAS'),
   path('list_ME/', list_meta, name='list_ME'),
   path('add_ME/',  create_meta, name='add_ME'),
   path('delete_ME/', delete_meta, name='delete_ME'),
   path('editar_ME/', editar_meta, name='editar_ME'),
   path('delect_checkbox_ME/', delete_checkbox_meta, name='delect_checkbox_ME'),
]
