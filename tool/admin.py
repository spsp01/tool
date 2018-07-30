from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Client,RaportScreaming,RaportScreamingtest

admin.site.register(Client)
admin.site.register(RaportScreaming)
#admin.site.register(Person)



@admin.register(RaportScreamingtest)
class RaportScreamingAdmin(ImportExportModelAdmin):
    pass
# Register your models here.
