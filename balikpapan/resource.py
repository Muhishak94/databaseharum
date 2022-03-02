from import_export import resources
from balikpapan.models import Balikpapan
from import_export.fields import Field


class BalikpapanResource(resources.ModelResource):
    class Meta:
        model = Balikpapan
