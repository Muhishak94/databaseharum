from django.urls import path

from . import views

urlpatterns = [
    path('dpt/input/', views.tambah_mahulu, name='tambah_mahulu'),
    path('dpt/update/<int:id_mahulu>', views.ubah_mahulu, name='ubah_mahulu'),
    path('hapus/<int:id_mahulu>', views.hapus_mahulu, name="hapus_mahulu"),
    path('export/xls/', views.export_xls, name='export_xls'),
    path('database/', views.mahulu, name='mahulu'),
    path('', views.index, name='infomahulu'),
]
