# coding=utf-8
from django.db import models

from brand_new_clinic.choices import MATERIAL_SUPPLIES_GROUP_CHOICE, POSITION_CATEGORY_CHOICE, YEAR_CHOICES, OS_GROUP


class PositionModel(models.Model):
    name = models.CharField(u'Наименование должности', max_length=50)
    category = models.CharField(u'Категория должности', choices=POSITION_CATEGORY_CHOICE, max_length=15)
    salary = models.IntegerField(u'Заработная плата', default=0)
    year = models.IntegerField(u'Год', choices=YEAR_CHOICES)

    class Meta:
        verbose_name = u'Справочник "Должности"'
        verbose_name_plural = u'Справочники "Должности"'


class MedicalSuppliesModel(models.Model):
    name = models.CharField(u'Наименование', max_length=100)
    supply_unit = models.CharField(u'Едининица поставки', max_length=50)  # TYPE
    write_off_unit = models.CharField(u'Единица списания (минимальная)', max_length=50)  # TYPE
    count = models.IntegerField(u'Количество в удинице поставки')
    material_group = models.IntegerField(u'Группа материальных запасов', choices=MATERIAL_SUPPLIES_GROUP_CHOICE)

    class Meta:
        verbose_name = u'Справочник "Медицинские запасы"'
        verbose_name_plural = u'Справочники "Медицинские запасы"'


class MainCureModel(models.Model):
    name = models.CharField(u'Наименование основного средства', max_length=100)
    os_group = models.CharField(u'Группа ОС', choices=OS_GROUP, max_length=100)
    good_using_time_start = models.DateTimeField(u'Начало срока полезного действия')
    good_using_time_end = models.DateTimeField(u'Окончание срока полезного действия')

    class Meta:
        verbose_name = u'Справочник "Основные средства"'
        verbose_name_plural = u'Справочники "Основные средства"'


class DrugsModel(models.Model):
    ath_classification = models.CharField(u'АТХ-классификация', max_length=100)   # TYPE
    mnn = models.IntegerField(u'МНН')   # TYPE
    commercial_name = models.CharField(u'Торговое наименование', max_length=100)
    supply_unit = models.CharField(u'Единица поставки ЕДпост', max_length=100)  # TYPE
    write_off_unit = models.CharField(u'Единица списания (минимальная) ЕДмин', max_length=100)   # TYPE
    count_edpost = models.IntegerField(u'Количество в ЕДпост', default=0)   # TYPE
    count_active_sub = models.IntegerField(u'Количество ДействВещ в ЕДмин', default=0)   # TYPE
    farm_group = models.IntegerField(u'Фармокологическая группа', default=0)     # TYPE

    class Meta:
        verbose_name = u'Справочник "Лекартственные средства"'
        verbose_name_plural = u'Справочники "Лекартственные средства"'
