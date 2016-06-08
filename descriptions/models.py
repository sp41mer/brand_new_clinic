# coding=utf-8
from django.db import models
from brand_new_clinic.choices import SERVICE_TYPE_CHOICE
from enchiridions.models import PositionModel, MainCureModel, MedicalSuppliesModel, DrugsModel


class WorkDescriptionModel(models.Model):
    position = models.ForeignKey(PositionModel, verbose_name=u'Должность')
    time_type = models.CharField(u'Единица измерения времени рабты', max_length=30)
    count = models.IntegerField(u'Количество', default=0)
    fold = models.FloatField(u'Кратность (вероятность участия сотрудника при оказании услуги)', default=0)


class EquipmentDescriptionModel(models.Model):
    cure = models.ForeignKey(MainCureModel, verbose_name=u'Основное средство')
    time_type = models.CharField(u'Единица измерения времени рабты', max_length=30)
    count = models.IntegerField(u'Количество', default=0)
    fold = models.FloatField(u'Кратность (вероятность применения оборудования при оказании услуги)', default=0)


class SuppliesDescriptionModel(models.Model):
    supplies = models.ForeignKey(MedicalSuppliesModel, verbose_name=u'Наименование материального запаса')
    time_type = models.CharField(u'Единица измерения', max_length=30)
    count = models.IntegerField(u'Количество', default=0)
    fold = models.FloatField(u'Кратность (вероятность применения материального запаса при оказании услуги)', default=0)


class DrugsDescription(models.Model):
    drug = models.ForeignKey(DrugsModel, verbose_name=u'Лекартвенное средство')
    count = models.IntegerField(u'Количество', default=0)
    fold = models.FloatField(u'Кратность (вероятность участия применения лекарственного средства при оказании услуги)', default=0)


class MethodDrugsDescription(models.Model):
    drug = models.ForeignKey(DrugsModel, verbose_name=u'Лекартвенное средство')
    fold = models.FloatField(u'Кратность назначения', default=0)
    unit = models.CharField(u'Единица измерения', max_length=20)
    dose_avg_day = models.IntegerField(u'Средняя суточная доза', default=0)
    dose_avg_course = models.IntegerField(u'Средняя курсовая доза', default=0)


class ServiceDescription(models.Model):
    type = models.CharField(u'Вид услуги', choices=SERVICE_TYPE_CHOICE, max_length=15)
    code = models.IntegerField(u'Код услуги')    # TYPE
    service_name = models.CharField(u'Наименование услуги', max_length=100)
    work_decsr = models.ForeignKey(WorkDescriptionModel)
    equipment_descr = models.ForeignKey(EquipmentDescriptionModel)
    supplies_descr = models.ForeignKey(SuppliesDescriptionModel)
    drugs_descr = models.ForeignKey(DrugsDescription)
