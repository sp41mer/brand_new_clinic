# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='nutritionalcare',
            options={'verbose_name': '\u0412\u0438\u0434 \u043b\u0435\u0447\u0435\u0431\u043d\u043e\u0433\u043e \u043f\u0438\u0442\u0430\u043d\u044f', 'verbose_name_plural': '\u0412\u0438\u0434\u044b \u043b\u0435\u0447\u0435\u0431\u043d\u043e\u0433\u043e \u043f\u0438\u0442\u0430\u043d\u0438\u044f'},
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name': '\u0421\u043f\u0438\u0441\u043e\u043a \u0443\u0441\u043b\u0443\u0433', 'verbose_name_plural': '\u0421\u043f\u0438\u0441\u043a\u0438 \u0443\u0441\u043b\u0443\u0433'},
        ),
        migrations.AlterModelOptions(
            name='treatmentdescriptionmodel',
            options={'verbose_name': '\u041c\u0435\u0442\u043e\u0434 \u043b\u0435\u0447\u0435\u043d\u0438\u044f', 'verbose_name_plural': '\u041c\u0435\u0442\u043e\u0434\u044b \u043b\u0435\u0447\u0435\u043d\u0438\u044f'},
        ),
    ]
