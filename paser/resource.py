from import_export import resources
from paser.models import Paser
from import_export.fields import Field


class PaserResource(resources.ModelResource):
    class Meta:
        model = Paser
