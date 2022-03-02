from django.urls import path

from . import views

urlpatterns = [
    path('dpt/input/', views.tambah_samarinda, name='tambah_samarinda'),
    path('dpt/update/<int:id_samarinda>',
         views.ubah_samarinda, name='ubah_samarinda'),
    path('hapus/<int:id_samarinda>', views.hapus_samarinda, name="hapus_samarinda"),
    path('export/xls/', views.export_xls, name='export_xls'),
    path('database/', views.samarinda, name='samarinda'),
    path('', views.index, name='infosamarinda'),
]
