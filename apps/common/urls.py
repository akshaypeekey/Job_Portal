"""jobportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from apps.common.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', HomeView.as_view(), name='home'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('add_company/', CompanyAddView.as_view(), name='add_company'),
    path('edit_company/<str:id>/', CompanyUpdateView.as_view(), name='edit_company'),
    path('view_company/', CompanyView.as_view(), name='view_company'),
    path('details_company/<str:id>', CompanyDetail.as_view(), name='details_company'),

]
