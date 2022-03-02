from django.urls import path

from . import views

urlpatterns = [
    path('dpt/input/', views.tambah_kubar, name='tambah_kubar'),
    path('dpt/update/<int:id_kubar>',
         views.ubah_kubar, name='ubah_kubar'),
    path('hapus/<int:id_kubar>', views.hapus_kubar, name="hapus_kubar"),
    path('export/xls/', views.export_xls, name='export_xls'),
    path('database/', views.kubar, name='kubar'),
    path('', views.index, name='infokubar'),
]
