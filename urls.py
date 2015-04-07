from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from dashboard.views import BarView
from django.views.generic import TemplateView


admin.site.site_title = _("TextAlytics")
admin.site.site_header = _("Adminsitrador TextAlytics")
admin.site.index_title = _("Configuracion de TextAlytics")

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'analitycs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', TemplateView.as_view(template_name="dashboard/index.html")),
    url(r'^admin/', include(admin.site.urls), name="index"),
    url(r'^data/', BarView.as_view(), name='data'),
    url(r'^grappelli/', include('grappelli.urls')),
)
