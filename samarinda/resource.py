from import_export import resources
from samarinda.models import Samarinda
from import_export.fields import Field


class SamarindaResource(resources.ModelResource):
    class Meta:
        model = Samarinda
