from django.contrib import admin

from core.models import FAQ, Technology, Service, Testimonial, CSCategory, CaseStudy, Contact, GetQuote, SEOHomepage

# Register your models here.

class TechnologyAdmin(admin.ModelAdmin):
    list_display = ['title', 'logo']

class ServiceAdmin(admin.ModelAdmin):
    list_display = ['heading', 'description']

class CSCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    readonly_fields = ['slug']

class CaseStudyAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'category']
    readonly_fields = ['slug']

class FAQAdmin(admin.ModelAdmin):
    list_display = ['question']

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'profession', 'rating']

class ContactAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'phone']

class GetQuoteAdmin(admin.ModelAdmin):
    list_display = ['email',]

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
admin.site.register(SEOHomepage, SEOHomepageAdmin)