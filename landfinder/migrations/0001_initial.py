# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-05 18:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LandPlot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=50, verbose_name='\u041d\u043e\u043c\u0435\u0440')),
                ('name', models.CharField(max_length=100, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('square', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='\u041f\u043b\u043e\u0449\u0430\u0434\u044c')),
                ('price', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='\u041a\u0430\u0434\u0430\u0441\u0442\u0440\u043e\u0432\u0430\u044f \u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c')),
            ],
        ),
    ]
