from django.urls import path, re_path

from . import views

urlpatterns = [
    path('input/', views.input),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
    # path('update/<int:id>/', views.update, name='update'),
    # path('update/<int:id>/', views.update, name='update'),
    path('', views.index, name='database'),
    path('export/xls/', views.export_xls, name='export_xls'),
]
