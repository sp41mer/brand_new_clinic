# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('descriptions', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='drugsdescription',
            options={'verbose_name': '\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043b\u0435\u043a\u0440\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0445 \u0441\u0440\u0435\u0434\u0441\u0442\u0432', 'verbose_name_plural': '\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u044f \u043b\u0435\u043a\u0440\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0445 \u0441\u0440\u0435\u0434\u0441\u0442\u0432'},
        ),
        migrations.AlterModelOptions(
            name='equipmentdescriptionmodel',
            options={'verbose_name': '\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043e\u0431\u043e\u0440\u0443\u0434\u043e\u0432\u0430\u043d\u0438\u044f', 'verbose_name_plural': '\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u044f \u043e\u0431\u043e\u0440\u0443\u0434\u043e\u0432\u0430\u043d\u0438\u044f'},
        ),
        migrations.AlterModelOptions(
            name='methoddrugsdescription',
            options={'verbose_name': '\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043f\u0440\u0438\u043c\u0435\u043d\u0435\u043d\u0438\u044f \u043b\u0435\u043a\u0440\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0445 \u0441\u0440\u0435\u0434\u0441\u0442\u0432', 'verbose_name_plural': '\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u044f \u043f\u0440\u0438\u043c\u0435\u043d\u0435\u043d\u0438\u044f \u043b\u0435\u043a\u0440\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0445 \u0441\u0440\u0435\u0434\u0441\u0442\u0432'},
        ),
        migrations.AlterModelOptions(
            name='servicedescription',
            options={'verbose_name': '\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0443\u0441\u043b\u0443\u0433\u0438', 'verbose_name_plural': '\u041e\u043f\u0438\u0441\u0430\u043d\u044f \u0443\u0441\u043b\u0443\u0433\u0438'},
        ),
        migrations.AlterModelOptions(
            name='suppliesdescriptionmodel',
            options={'verbose_name': '\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u044c\u043d\u044b\u0445 \u0437\u0430\u043f\u0430\u0441\u043e\u0432', 'verbose_name_plural': '\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u044f \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u044c\u043d\u044b\u0445 \u0437\u0430\u043f\u0430\u0441\u043e\u0432'},
        ),
        migrations.AlterModelOptions(
            name='workdescriptionmodel',
            options={'verbose_name': '\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0440\u0430\u0431\u043e\u0442\u044b \u0432\u0441\u0435\u0445 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u043e\u0432', 'verbose_name_plural': '\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u044f \u0440\u0430\u0431\u043e\u0442\u044b \u0432\u0441\u0435\u0445 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u043e\u0432'},
        ),
        migrations.AlterField(
            model_name='servicedescription',
            name='drugs_descr',
            field=models.ForeignKey(verbose_name='\u041b\u0435\u043a\u0430\u0440\u0442\u0441\u0432\u0435\u043d\u043d\u043e\u0435 \u0441\u0440\u0435\u0434\u0441\u0442\u0432\u043e', to='descriptions.DrugsDescription'),
        ),
        migrations.AlterField(
            model_name='servicedescription',
            name='equipment_descr',
            field=models.ForeignKey(verbose_name='\u041e\u0431\u043e\u0440\u0443\u0434\u043e\u0432\u0430\u043d\u0438\u0435', to='descriptions.EquipmentDescriptionModel'),
        ),
        migrations.AlterField(
            model_name='servicedescription',
            name='supplies_descr',
            field=models.ForeignKey(verbose_name='\u041c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u044c\u043d\u044b\u0435 \u0437\u0430\u043f\u0430\u0441\u044b', to='descriptions.SuppliesDescriptionModel'),
        ),
        migrations.AlterField(
            model_name='servicedescription',
            name='work_decsr',
            field=models.ForeignKey(verbose_name='\u0420\u0430\u0431\u043e\u0442\u0430', to='descriptions.WorkDescriptionModel'),
        ),
    ]
