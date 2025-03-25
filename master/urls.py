from django.urls import path

from .views import master_view

app_name = "master"
urlpatterns = [
   path('dashboard/', master_view, name='master'),
]