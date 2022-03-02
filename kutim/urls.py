from django.urls import path

from . import views

urlpatterns = [
    path('dpt/input/', views.tambah_kutim, name='tambah_kutim'),
    path('dpt/update/<int:id_kutim>',
         views.ubah_kutim, name='ubah_kutim'),
    path('hapus/<int:id_kutim>', views.hapus_kutim, name="hapus_kutim"),
    path('export/xls/', views.export_xls, name='export_xls'),
    path('database/', views.kutim, name='kutim'),
    path('', views.index, name='infokutim'),
]
