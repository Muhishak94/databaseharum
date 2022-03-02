from django.urls import path

from . import views

urlpatterns = [
    path('dpt/input/', views.tambah_balikpapan, name='tambah_balikpapan'),
    path('dpt/update/<int:id_balikpapan>', views.ubah_balikpapan, name='ubah_balikpapan'),
    path('hapus/<int:id_balikpapan>', views.hapus_balikpapan, name="hapus_balikpapan"),
    path('export/xls/', views.export_xls, name='export_xls'),
    path('database/', views.balikpapan, name='balikpapan'),
    path('', views.index, name='infobalikpapan'),
]
