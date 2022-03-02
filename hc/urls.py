from django.urls import path

from . import views

urlpatterns = [
    path('kota/', views.kota, name='kota'),
    path('infopemilu/', views.infopemilu, name='infopemilu'),
    path('', views.index, name='harumcenter'),
]
