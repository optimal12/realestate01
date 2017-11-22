from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import City, Neighborhood, Property, Surfer
# Register your models here.
admin.site.register(City)
admin.site.register(Neighborhood)
admin.site.register(Property,ImportExportModelAdmin)
admin.site.register(Surfer,ImportExportModelAdmin)
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
#from import_export.admin import ImportExportModelAdmin
#from django.contrib import admin
#from .models import Property

class PropertyAdmin(ImportExportModelAdmin):
    pass
class SurferAdmin(ImportExportModelAdmin):
    pass
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
#admin.site.register(Prices, PriceAdmin)
