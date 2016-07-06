# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import permalink


class LandPlot(models.Model):
    number = models.CharField(u'Номер', max_length=50)
    name = models.CharField(u'Название', max_length=100)
    square = models.DecimalField(u'Площадь', max_digits=15, decimal_places=2)
    price = models.DecimalField(u'Кадастровая стоимость', max_digits=15, decimal_places=2)

    @permalink
    def get_absolute_url(self):
        return 'plot-info', [self.pk]

    @permalink
    def qr_code_url(self):
        return 'plot-qr', [self.pk]
