"""BravoFC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from home.views import home_view
from teams.views import team_list_view, team_detail_view, team_create_view

urlpatterns = [
    path('', home_view, name='home'),
    path('teams/', team_detail_view, name='team_list'),
    # path('teams/a', team_detail_view, name='team_detail'),
    path('teams/create/', team_create_view, name='team_create'),
    path('admin/', admin.site.urls),
]
