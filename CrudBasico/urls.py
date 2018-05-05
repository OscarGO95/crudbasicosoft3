"""iteracion0 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from appcrudbasico import views
urlpatterns = [
    path('',views.estudiante),
    path('admin/', admin.site.urls),
    path(r'estudiante/list/', views.estudiante, name='list_estudiante'), #listado
    path(r'estudiante/add/', views.add_estudiante, name='add_estudiante'), #formulario para añadir
    path(r'estudiante/<int:id>/', views.update_estudiante, name='update_estudiante'), #formulario para editar
    path(r'estudiante/delete/<int:id>/', views.delete_estudiante, name='delete_estudiante'), #ruta para eliminar
]

