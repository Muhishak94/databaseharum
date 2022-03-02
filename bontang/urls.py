from django.urls import path

from . import views

urlpatterns = [
    path('dpt/input/', views.tambah_bontang, name='tambah_bontang'),
    path('dpt/update/<int:id_bontang>',
         views.ubah_bontang, name='ubah_bontang'),
    path('hapus/<int:id_bontang>', views.hapus_bontang, name="hapus_bontang"),
    path('export/xls/', views.export_xls, name='export_xls'),
    path('database/', views.bontang, name='bontang'),
    path('', views.index, name='infobontang'),
]
