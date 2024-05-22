from core.views import ajax_contact_form, ajax_get_quote, index, portfolio
from django.urls import path
from django.contrib.sitemaps.views import sitemap
from .sitemap import StaticViewSitemap, CaseStudySitemap

app_name = "core"

sitemaps = {
    "static": StaticViewSitemap,
    'case-study': CaseStudySitemap,
}

urlpatterns = [
    path("", index, name="index"),
    path("case-study/<slug>/", portfolio, name="case-study"),
    path("ajax-contact-form/", ajax_contact_form, name="ajax-contact-form"),
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