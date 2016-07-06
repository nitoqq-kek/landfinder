# -*- coding: utf-8 -*-
from decimal import Decimal

from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.core.management.base import BaseCommand

from landfinder.models import LandPlot


class Command(BaseCommand):
    def handle(self, *args, **options):
        if not settings.DEBUG:
            raise RuntimeError('Impossible to run in production!')
        LandPlot.objects.all().delete()
        LandPlot.objects.bulk_create((
            LandPlot(number='number-%s' % x, name='plot-%s' % x, square=Decimal('%s0.50' % x),
                     price=Decimal('10%s0.00' % x)) for x in xrange(800)
        ))
        print 'Land plots were created\n'
        Site.objects.filter(id=settings.SITE_ID).update(domain='localhost:8000', name='localhost:8000')
        print 'Default site domain was replaced to localhost:8000\n'

        User.objects.filter(username__in=('superuser', 'simpleuser')).delete()

        user = User.objects.create(username='superuser', is_staff=True, is_superuser=True)
        user.set_password('hodorhodor')
        user.save()

        user = User.objects.create(username='simpleuser')
        user.set_password('hodorhodor')
        user.save()

        print 'Test users were created:'
        print '\tusername: superuser \n\tpassword: hodorhodor'
        print '\n\tusername: simpleuser \n\tpassword: hodorhodor'
