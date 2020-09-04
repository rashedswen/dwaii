
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
# Register your models here.
from medicine.models import storage, medicine, user_info, requestMedi, location, medType, medCategory, pharmacyAcc, \
    CustomerAcc, organizationAcc

admin.site.register(user_info)
admin.site.register(storage)
admin.site.register(requestMedi)
admin.site.register(medType)
admin.site.register(medCategory)
admin.site.register(location)
admin.site.register(pharmacyAcc)
admin.site.register(CustomerAcc)
admin.site.register(organizationAcc)

@admin.register(medicine)
class ViewAdmin(ImportExportModelAdmin):
    pass

