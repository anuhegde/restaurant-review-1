from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Restaurant
from .models import Person


@admin.register(Restaurant)
class RestaurantAdmin(ImportExportModelAdmin):
    pass

@admin.register(Person)
class PersonAdmin(ImportExportModelAdmin):
    pass
