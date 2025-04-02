"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('login.urls')),
    path('master/', include('master.urls'),name="master"),
    path('master/list/list_OE/add/', include('master.urls'),name="create_OE"),
    path('master/list/', include('master.urls'),name="master_list"),
    path('master/list/list_OE/editar/', include('master.urls'),name="editar_OE"),
    path('master/list/list_OE/delete/', include('master.urls'),name="delete_OE"),
    path('master/list/list_OE/delect_checkbox/', include('master.urls'),name="delect_checkbox_OE"),
    path('master/list/list_RAS/add/', include('master.urls'),name="add_ras"),
    path('master/list/list_RAS/editar/', include('master.urls'),name="editar_RAS"),
    path('master/list/list_RAS/delete/', include('master.urls'),name="delete_RAS"),  
    path('master/list/list_RAS/delect_checkbox/', include('master.urls'),name="delect_checkbox_RAS"),
    path('master/list/list_ME/add/', include('master.urls'),name="add_ME"),    
    path('master/list/list_ME/delete/', include('master.urls'),name="delete_ME"),
    path('master/list/list_ME/editar/', include('master.urls'),name="editar_ME"),
    path('master/list/list_ME/delect_checkbox/', include('master.urls'),name="delect_checkbox"),
    path('master/list/list_KPI/add/', include('master.urls'),name="add_kpi"),
    path('master/list/list_KPI/editar/', include('master.urls'),name="list_KPI"),
    path('master/list/list_KPI/delete/', include('master.urls'),name="delete_KPI"),  
    path('master/list/list_KPI/delect_checkbox/', include('master.urls'),name="delect_checkbox"),
    path('master/list/list_OA/add/', include('master.urls'),name="add_OA"),    
    path('master/list/list_OA/editar/', include('master.urls'),name="editar_OA"),
    path('master/list/list_OA/delete/', include('master.urls'),name="delete_OA"),
    path('master/list/list_OA/delect_checkbox/', include('master.urls'),name="delect_checkbox"),   
    path('master/list/list_AAN/add/', include('master.urls'),name="add_AAN"),    
    path('master/list/list_AAN/editar/', include('master.urls'),name="editar_AAN"),
    path('master/list/list_AAN/delete/', include('master.urls'),name="delete_AAN"),
    path('master/list/list_AAN/delect_checkbox/', include('master.urls'),name="delect_checkbox"),   
    path('master/list/list_AC/add/', include('master.urls'),name="add_AC"),   
    path('master/list/list_AC/editar/', include('master.urls'),name="editar_AC"),
    path('master/list/list_AC/delete/', include('master.urls'),name="delete_AC"),
    path('master/list/list_AC/delect_checkbox/', include('master.urls'),name="delect_checkbox"),
    path('departamento/', include('departamentos.urls'),name="departamento"),
  ]
