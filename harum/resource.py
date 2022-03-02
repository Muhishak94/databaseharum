from import_export import resources
from harum.models import Database, Kelurahan


class DatabaseResource(resources.ModelResource):
    class Meta:
        model = Database
        # bisa ditentukan kolom apa saja yang bisa export pada video link berikut di menit 6:14 https://www.youtube.com/watch?v=ICI6OXkr7Vk&list=PLSCLBARdXrOz4SM3GKyKuqQp7eXWAH1u1&index=31
        # field = ['kota', 'kelurahan',] untuk memilih file apa saja yang akan di dwonload
        # export_order = ['kota__nama', 'kelurahan',] untuk urutkan dan tanda "__" khusus untuk data yang korelasi/foreign key
