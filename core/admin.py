from django.contrib import admin
from django.utils.html import format_html
from django_json_widget.widgets import JSONEditorWidget
from django.db import models
from core.models import FAQ, Technology, Service, Testimonial, CSCategory, CaseStudy, Contact, GetQuote, SEOHomepage, ServiceFAQ, ServiceHighlight, ServiceTechnicalHighlight, ServiceSection1, ServiceSection2, ServicePageLead

# Register your models here.

class ServiceFAQInline(admin.StackedInline):
    model = ServiceFAQ
    extra = 1

class ServiceHighlightsInline(admin.StackedInline):
    model = ServiceHighlight
    extra = 1

class ServiceTechnicalsInline(admin.StackedInline):
    model = ServiceTechnicalHighlight
    extra = 1

class ServiceSection1Inline(admin.StackedInline):
    model = ServiceSection1

class ServiceSection2Inline(admin.StackedInline):
    model = ServiceSection2

class TechnologyAdmin(admin.ModelAdmin):
    list_display = ['title', 'logo']

class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'date']
    inlines = [ServiceHighlightsInline, ServiceSection1Inline, ServiceTechnicalsInline, ServiceSection2Inline, ServiceFAQInline]

class CSCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    readonly_fields = ['slug']

class CaseStudyAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'category', 'status']
    readonly_fields = ['slug']

class FAQAdmin(admin.ModelAdmin):
    list_display = ['question']

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'profession', 'rating']

class ContactAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'phone']

class GetQuoteAdmin(admin.ModelAdmin):
    list_display = ['email',]

    def get_readonly_fields(self, request, obj=None):
        return [field.name for field in self.model._meta.fields]

class ServiceLeadAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'page_url']

    def get_readonly_fields(self, request, obj=None):
        return [field.name for field in self.model._meta.fields]

class SEOHomepageAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']

admin.site.register(Technology, TechnologyAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(CaseStudy, CaseStudyAdmin)
admin.site.register(CSCategory, CSCategoryAdmin)
admin.site.register(FAQ, FAQAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(GetQuote, GetQuoteAdmin)
admin.site.register(ServicePageLead, ServiceLeadAdmin)
admin.site.register(SEOHomepage, SEOHomepageAdmin)