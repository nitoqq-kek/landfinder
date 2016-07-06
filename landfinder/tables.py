# -*- coding: utf-8 -*-
from django_tables2 import tables, columns, A
from landfinder.models import LandPlot


class IndexTable(tables.Table):

    detail = columns.LinkColumn('plot-info', empty_values=(), verbose_name=u'Название', args=[A('pk')], text=lambda r: r.name, order_by='name')

    class Meta:
        model = LandPlot
        per_page = 20
        fields = sequence = ('number', 'detail', 'square', )
        template = 'django_tables2/bootstrap.html'
