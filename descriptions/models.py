# coding=utf-8
from django.db import models
from brand_new_clinic.choices import SERVICE_TYPE_CHOICE
from enchiridions.models import PositionModel, MainCureModel, MedicalSuppliesModel, DrugsModel


class WorkDescriptionModel(models.Model):
    position = models.ForeignKey(PositionModel, verbose_name=u'Должность')
    time_type = models.CharField(u'Единица измерения времени рабты', max_length=30)
    count = models.IntegerField(u'Количество', default=0)
    fold = models.FloatField(u'Кратность (вероятность участия сотрудника при оказании услуги)', default=0)

    class Meta:
        verbose_name = u'Описание работы всех сотрудников'
        verbose_name_plural = u'Описания работы всех сотрудников'

    def __unicode__(self):
        return "{}".format(self.name)


class EquipmentDescriptionModel(models.Model):
    cure = models.ForeignKey(MainCureModel, verbose_name=u'Основное средство')
    time_type = models.CharField(u'Единица измерения времени рабты', max_length=30)
    count = models.IntegerField(u'Количество', default=0)
    fold = models.FloatField(u'Кратность (вероятность применения оборудования при оказании услуги)', default=0)

    class Meta:
        verbose_name = u'Описание оборудования'
        verbose_name_plural = u'Описания оборудования'

    def __unicode__(self):
        return "{}".format(self.name)


class SuppliesDescriptionModel(models.Model):
    supplies = models.ForeignKey(MedicalSuppliesModel, verbose_name=u'Наименование материального запаса')
    time_type = models.CharField(u'Единица измерения', max_length=30)
    count = models.IntegerField(u'Количество', default=0)
    fold = models.FloatField(u'Кратность (вероятность применения материального запаса при оказании услуги)', default=0)

    class Meta:
        verbose_name = u'Описание материальных запасов'
        verbose_name_plural = u'Описания материальных запасов'

    def __unicode__(self):
        return "{}".format(self.name)


class DrugsDescription(models.Model):
    drug = models.ForeignKey(DrugsModel, verbose_name=u'Лекартвенное средство')
    count = models.IntegerField(u'Количество', default=0)
    fold = models.FloatField(u'Кратность (вероятность участия применения лекарственного средства при оказании услуги)', default=0)

    class Meta:
        verbose_name = u'Описание лекрственных средств'
        verbose_name_plural = u'Описания лекрственных средств'

    def __unicode__(self):
        return "{}".format(self.name)


class MethodDrugsDescription(models.Model):
    drug = models.ForeignKey(DrugsModel, verbose_name=u'Лекартвенное средство')
    fold = models.FloatField(u'Кратность назначения', default=0)
    unit = models.CharField(u'Единица измерения', max_length=20)
    dose_avg_day = models.IntegerField(u'Средняя суточная доза', default=0)
    dose_avg_course = models.IntegerField(u'Средняя курсовая доза', default=0)

    class Meta:
        # TODO: fix naming
        verbose_name = u'Описание применения лекрственных средств'
        verbose_name_plural = u'Описания применения лекрственных средств'

    def __unicode__(self):
        return "{}".format(self.name)


class ServiceDescription(models.Model):
    type = models.CharField(u'Вид услуги', choices=SERVICE_TYPE_CHOICE, max_length=15)
    code = models.IntegerField(u'Код услуги')    # TYPE
    service_name = models.CharField(u'Наименование услуги', max_length=100)
    work_decsr = models.ForeignKey(WorkDescriptionModel, verbose_name=u'Работа')
    equipment_descr = models.ForeignKey(EquipmentDescriptionModel, verbose_name=u'Оборудование')
    supplies_descr = models.ForeignKey(SuppliesDescriptionModel, verbose_name=u'Материальные запасы')
    drugs_descr = models.ForeignKey(DrugsDescription, verbose_name=u'Лекартсвенное средство')

    class Meta:
        verbose_name = u'Описание услуги'
        verbose_name_plural = u'Описаня услуги'

    def __unicode__(self):
        return "{}".format(self.name)
