from django.contrib import admin
from harum.models import Database, Kota, Kecamatan, Kelurahan, Hasil_Telespocheck, Status_Telespocheck, Telespochecker, Inputer

# Register your models here.


# class DisplayAdmin(admin.ModelAdmin):
#     list_display = ['id', 'kota', 'kecamatan', 'kelurahan',
#                     'nama_dpt', 'nik', 'hasil_telespocheck', ]
#     search_fields = ['id', 'kota', 'kecamatan',
#                      'kelurahan', 'nama_dpt', 'nik', 'no_kk', 'hasil_telespocheck', ]
#     list_filter = ('kota', 'kecamatan', 'kelurahan',)
#     list_per_page = 10


# admin.site.register(Database, DisplayAdmin)
# admin.site.register(Kota)
# admin.site.register(Kecamatan)
# admin.site.register(Kelurahan)
# admin.site.register(Hasil_Telespocheck)
# admin.site.register(Status_Telespocheck)
# admin.site.register(Telespochecker)
# admin.site.register(Inputer)
