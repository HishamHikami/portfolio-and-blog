from core.views import ajax_contact_form, ajax_get_quote, index, portfolio
from django.urls import path

app_name = "core"

urlpatterns = [
    path("", index, name="index"),
    path("case-study/<slug>/", portfolio, name="case-study"),
    path("ajax-contact-form/", ajax_contact_form, name="ajax-contact-form"),
    path("ajax-get-quote/", ajax_get_quote, name="ajax-get-quote"),
]