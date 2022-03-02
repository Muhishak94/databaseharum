from django.urls import path

from . import views

urlpatterns = [
    path('dpt/input/', views.tambah_kukar, name='tambah_kukar'),
    path('dpt/update/<int:id_kukar>',
         views.ubah_kukar, name='ubah_kukar'),
    path('hapus/<int:id_kukar>', views.hapus_kukar, name="hapus_kukar"),
    path('export/xls/', views.export_xls, name='export_xls'),
    path('database/', views.kukar, name='kukar'),
    path('', views.index, name='infokukar'),
]
