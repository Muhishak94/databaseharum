from django.urls import path

from . import views

urlpatterns = [
    path('dpt/input/', views.tambah_berau, name='tambah_berau'),
    path('dpt/update/<int:id_berau>',
         views.ubah_berau, name='ubah_berau'),
    path('hapus/<int:id_berau>', views.hapus_berau, name="hapus_berau"),
    path('export/xls/', views.export_xls, name='export_xls'),
    path('database/', views.berau, name='berau'),
    path('', views.index, name='infoberau'),
]
