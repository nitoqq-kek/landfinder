from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
import django.contrib.auth.views
import landfinder.views


admin.autodiscover()

urlpatterns = [
    url(r'^$', landfinder.views.index, name='index'),
    url(r'^info/(?P<plot_id>\d+)$', landfinder.views.plot_info, name='plot-info'),
    url(r'^qr-code/(?P<plot_id>\d+)\.png$', landfinder.views.plot_qr, name='plot-qr'),
    url(r'^login/$', landfinder.views.login, name='login'),
    url(r'^logout/$', django.contrib.auth.views.logout, name='logout'),
    url(r'^admin/', admin.site.urls),

]

if settings.DEBUG:
    from django.conf.urls.static import static
    for path, root in settings.STATIC_URLS:
        urlpatterns += static(path, document_root=root)
