from import_export import resources
from perpustakaan.models import Buku
from import_export.fields import Field


class BukuResource(resources.ModelResource):
    class Meta:
        model = Buku
