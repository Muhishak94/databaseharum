from import_export import resources
from ppu.models import Ppu
from import_export.fields import Field


class PpuResource(resources.ModelResource):
    class Meta:
        model = Ppu
