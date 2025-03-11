from core.views import ajax_contact_form, ajax_get_quote, index, portfolio, service_detail, service_detail_form_submit
from django.http import JsonResponse
from django.urls import path
from django.contrib.sitemaps.views import sitemap
from .sitemap import StaticViewSitemap, CaseStudySitemap, ServiceSitemap

app_name = "core"

sitemaps = {
    "static": StaticViewSitemap,
    'case-study': CaseStudySitemap,
    'service': ServiceSitemap,
}

urlpatterns = [
    path("", index, name="index"),
    path('service/<slug:slug>/', service_detail, name='service_detail'),
    path("case-study/<slug>/", portfolio, name="case-study"),
    path("ajax-contact-form/", ajax_contact_form, name="ajax-contact-form"),
    path("ajax-service-detail-form/", service_detail_form_submit, name="ajax-service-detail-form"),
    path("ajax-get-quote/", ajax_get_quote, name="ajax-get-quote"),
    path(
        "core-sitemap.xml",
        sitemap,
        {
            'sitemaps': sitemaps
        },
        name = 'django.contrib.sitemaps.views.sitemap'
    ),
]