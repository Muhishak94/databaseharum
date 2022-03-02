from import_export import resources
from mahulu.models import Mahulu
from import_export.fields import Field


class MahuluResource(resources.ModelResource):
    class Meta:
        model = Mahulu
