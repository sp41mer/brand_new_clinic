from django.db import models
from ..choices import MATERIAL_SUPPLIES_GROUP_CHOICE, POSITION_CATEGORY_CHOICE, YEAR_CHOICES, OS_GROUP


class PositionModel(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(choices=POSITION_CATEGORY_CHOICE)
    salary = models.IntegerField(default=0)
    year = models.IntegerField(max_length=4, choices=YEAR_CHOICES)


class MedicalSupplies(models.Model):
    name = models.CharField(max_length=100)
    supply_unit = models.CharField(max_length=50)  # TYPE
    write_off_unit = models.CharField(max_length=50)  # TYPE
    count = models.IntegerField()
    material_group = models.CharField(choices=MATERIAL_SUPPLIES_GROUP_CHOICE)


class MainCure(models.Model):
    name = models.CharField(max_length=100)
    os_group = models.CharField(choices=OS_GROUP)
    good_using_time_start = models.DateTimeField()
    good_using_time_end = models.DateTimeField()


class Drugs(models.Model):
    ath_classification = models.CharField(max_length=100)   # TYPE
    mnn = models.IntegerField()   # TYPE
    commercial_name = models.CharField(max_length=100)
    supply_unit = models.CharField(max_length=100)  # TYPE
    write_off_unit = models.CharField(max_length=100)   # TYPE
    count_edpost = models.IntegerField(default=0)   # TYPE
    count_active_sub = models.IntegerField(default=0)   # TYPE
    farm_group = models.IntegerField(default=0) # TYPE
