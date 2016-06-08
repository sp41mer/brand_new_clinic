from django.contrib import admin
from descriptions.models import WorkDescriptionModel, SuppliesDescriptionModel, DrugsDescription, MethodDrugsDescription, \
    ServiceDescription, EquipmentDescriptionModel

admin.site.register(WorkDescriptionModel)
admin.site.register(EquipmentDescriptionModel)
admin.site.register(SuppliesDescriptionModel)
admin.site.register(DrugsDescription)
admin.site.register(MethodDrugsDescription)
admin.site.register(ServiceDescription)
