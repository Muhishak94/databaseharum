from import_export import resources
from kukar.models import Kukar
from import_export.fields import Field


class KukarResource(resources.ModelResource):
    class Meta:
        model = Kukar
