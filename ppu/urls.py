from django.urls import path

from . import views

urlpatterns = [
    path('dpt/input/', views.tambah_ppu, name='tambah_ppu'),
    path('dpt/update/<int:id_ppu>',
         views.ubah_ppu, name='ubah_ppu'),
    path('hapus/<int:id_ppu>', views.hapus_ppu, name="hapus_ppu"),
    path('export/xls/', views.export_xls, name='export_xls'),
    path('database/', views.ppu, name='ppu'),
    path('', views.index, name='infoppu'),
]
