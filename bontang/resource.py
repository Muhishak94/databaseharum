from import_export import resources
from bontang.models import Bontang
from import_export.fields import Field


class BontangResource(resources.ModelResource):
    class Meta:
        model = Bontang
