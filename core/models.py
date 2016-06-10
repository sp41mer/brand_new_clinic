# coding=utf-8
from django.contrib.auth.models import User
from django.db import models

from descriptions.models import WorkDescriptionModel, EquipmentDescriptionModel, SuppliesDescriptionModel, \
    DrugsDescription, MethodDrugsDescription, ServiceDescription


class Service(models.Model):
    service = models.ForeignKey(ServiceDescription, verbose_name=u'Услуга')
    count = models.IntegerField(u'Количество', default=0)
    fold = models.FloatField(u'Кратность (вероятность назначение данной услуги)', default=0)

    class Meta:
        verbose_name = u'Список услуг'
        verbose_name_plural = u'Списки услуг'


class NutritionalCare(models.Model):
    name = models.CharField(u'Наименование', max_length=50)
    count = models.IntegerField(u'Количество', default=0)
    fold = models.FloatField(u'Кратность', default=0)

    class Meta:
        verbose_name = u'Вид лечебного питаня'
        verbose_name_plural = u'Виды лечебного питания'


class TreatmentDescriptionModel(models.Model):
    section = models.CharField(u'Раздел', max_length=50)
    group_number = models.IntegerField(u'№ группы ВМП', default=0)
    vmp_type_name = models.CharField(u'Наименование виде ВМП', max_length=50)
    mkb_code = models.IntegerField(u'Код по МЛБ - 10', default=0)
    patient_type = models.CharField(u'Модель пациента', max_length=30)
    treatment_type = models.CharField(u'Вид лечения', max_length=50)
    service_list = models.ManyToManyField(Service, verbose_name=u'Список услуг')
    drugs_decr = models.ForeignKey(MethodDrugsDescription, verbose_name=u'Описание лекартвенных средств',
                                   related_name='drugs')
    implant_descr = models.ForeignKey(SuppliesDescriptionModel, verbose_name=u'Описание имплантов',
                                      related_name='implant')
    blood_notblood_descr = models.ForeignKey(SuppliesDescriptionModel,
                                             verbose_name=u'Описание препаратов крови и кровозаменителей')
    nutritional_care = models.ForeignKey(NutritionalCare, verbose_name=u'Виды лечебного питания')
    cure_avg_time = models.IntegerField(u'Средняя продолжительность лечения', default=0)

    class Meta:
        verbose_name = u'Метод лечения'
        verbose_name_plural = u'Методы лечения'