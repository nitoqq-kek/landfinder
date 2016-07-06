# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.views import login as login_view

from landfinder.models import LandPlot
from landfinder.tables import IndexTable
from landfinder.utils import make_qr_code


def login(request, *args, **kwargs):
    kwargs.setdefault('template_name', 'login.html')
    if request.user.is_authenticated():
        return redirect('index')
    return login_view(request, *args, **kwargs)


@login_required
def index(request):
    plots = IndexTable(LandPlot.objects.all(), request=request)
    return render(request, 'index.html', {
        'plots': plots,
    })


@login_required
def plot_info(request, plot_id):
    plot = get_object_or_404(LandPlot, pk=plot_id)
    return render(request, 'plot_info.html', {
        'plot': plot
    })


@login_required
def plot_qr(request, plot_id):
    plot = get_object_or_404(LandPlot, pk=plot_id)
    current_site = get_current_site(request)
    scheme = request.is_secure() and "https://" or "http://"
    link = ''.join((scheme, current_site.domain, plot.get_absolute_url()))
    img = make_qr_code(link)
    response = HttpResponse(content_type="image/png")
    img.save(response, "PNG")
    return response
