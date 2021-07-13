from django.urls import path
from . import views

urlpatterns = [
    path('demo', views.index, name='demo'),
    path('new_interaction', views.index, name='new_interaction'),
    path('coloringPage/', views.coloringPage, name='coloringPage'),
    path('welcomepage/', views.welcomepage, name='welcomepage'),
    path('home/', views.home, name='home'),
    path('cattemplate/', views.cattemplate, name='cattemplate'),
    path('saved/', views.saved, name='saved'),
    path('settings/', views.settings, name='settings')
]
