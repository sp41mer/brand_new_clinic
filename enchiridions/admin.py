from django.contrib import admin
from enchiridions.models import PositionModel, MedicalSuppliesModel, MainCureModel, DrugsModel

admin.site.register(PositionModel)
admin.site.register(MedicalSuppliesModel)
admin.site.register(MainCureModel)
admin.site.register(DrugsModel)
