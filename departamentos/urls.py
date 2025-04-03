from django.urls import path

from .views import list_home,adicionar_balanco,editar_balanco

urlpatterns = [
     
     path('list_home/', list_home, name='list_home'),
     path('balanco_AC/', adicionar_balanco, name='adicionar_balanco'),
     path('balanco_editar/', editar_balanco, name='balanco_editar'),
]
