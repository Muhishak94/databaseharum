from django.contrib import admin
from django.urls import path, include
from perpustakaan.views import *
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hc/', include('hc.urls')),
    path('harum/', include('harum.urls')),
    path('pasar/', include('pasar.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
    path('paser/', include('paser.urls')),
    path('samarinda/', include('samarinda.urls')),
    path('balikpapan/', include('balikpapan.urls')),
    path('ppu/', include('ppu.urls')),
    path('mahulu/', include('mahulu.urls')),
    path('kubar/', include('kubar.urls')),
    path('kutim/', include('kutim.urls')),
    path('kukar/', include('kukar.urls')),
    path('bontang/', include('bontang.urls')),
    path('berau/', include('berau.urls')),
    path('penerbit/', penerbit, name='penerbit'),
    path('dpt/', buku, name='buku'),
    path('dpt/input/', tambah_buku, name='tambah_buku'),
    path('dpt/update/<int:id_buku>', ubah_buku, name='ubah_buku'),
    path('buku/hapus/<int:id_buku>', hapus_buku, name="hapus_buku"),
    path('buku/export/xls/', export_xls, name='export_xls'),
    path('auth/masuk/', LoginView.as_view(), name='masuk'),
    path('auth/keluar/', LogoutView.as_view(next_page='masuk'), name='keluar'),
    path('user/', users, name='users'),
    path('user/add/', signup, name='signup'),
    path('', views.index, name='dashboard'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
