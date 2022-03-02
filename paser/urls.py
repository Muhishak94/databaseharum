from django.urls import path

from . import views

urlpatterns = [
    path('dpt/input/', views.tambah_paser, name='tambah_paser'),
    path('dpt/update/<int:id_paser>', views.ubah_paser, name='ubah_paser'),
    path('hapus/<int:id_paser>', views.hapus_paser, name="hapus_paser"),
    path('export/xls/', views.export_xls, name='export_xls'),
    path('database/', views.paser, name='paser'),
    path('', views.index, name='infopaser'),
]
