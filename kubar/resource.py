from import_export import resources
from kubar.models import Kubar
from import_export.fields import Field


class KubarResource(resources.ModelResource):
    class Meta:
        model = Kubar
