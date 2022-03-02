from django.contrib import admin
from samarinda.models import Samarinda
from import_export.admin import ImportExportModelAdmin
# Register your models here.


@admin.register(Samarinda)
class ViewAdmin(ImportExportModelAdmin):
    list_display = ['id', 'kota', 'kecamatan', 'kelurahan',
                    'nama_dpt', 'nik', 'hasil_telespocheck', ]
    search_fields = ['id', 'kota', 'kecamatan',
                     'kelurahan', 'nama_dpt', 'nik', 'no_kk', 'hasil_telespocheck', ]
    list_filter = ('kota', 'kecamatan', 'kelurahan',)
    list_per_page = 990


# Register your models here.
