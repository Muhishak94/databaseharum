from import_export import resources
from berau.models import Berau
from import_export.fields import Field


class BerauResource(resources.ModelResource):
    class Meta:
        model = Berau
