from import_export import resources
from kutim.models import Kutim
from import_export.fields import Field


class KutimResource(resources.ModelResource):
    class Meta:
        model = Kutim
