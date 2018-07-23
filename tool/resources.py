from import_export import resources
from .models import Person,RaportScreamingtest

class PersonResource(resources.ModelResource):
    class Meta:
        model = Person

class RaportScreamingResource(resources.ModelResource):
    class Meta:
        model = RaportScreamingtest