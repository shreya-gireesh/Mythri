"""
URL configuration for Mythri project.

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
from tkinter.font import names

from django.contrib import admin
from django.urls import path
from UserApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('membership-form', views.membership_form, name='membership-form'),
    path('delete-member/<int:member_id>/', views.delete_member, name='delete-member'),
    path('add-member', views.addmember, name='add-member'),
    path('unit-creation', views.unitcreation, name='unit-creation'),
    path('zones', views.addzone, name='zones'),
    path('regions', views.addregion, name='regions'),
    path('areas', views.addarea, name='areas'),
    path('create-user', views.createuser, name='create-user'),
    path('members', views.members, name='members'),
    path('units', views.units, name='units'),
    path('unitpage/<int:unit_id>/', views.unitspage, name='unitpage'),
    path('report', views.report, name='report'),

    path('delete-zone/<int:zone_id>/', views.delete_zone, name='delete-zone'),
    path('delete-region/<int:region_id>/', views.delete_region, name='delete-region'),
    path('delete-area/<int:area_id>/', views.delete_area, name='delete-area'),
    path('delete-unit/<int:unit_id>/', views.delete_unit, name='delete-unit'),
    path('delete-user/<int:user_id>/', views.delete_user, name='delete-user'),

]
