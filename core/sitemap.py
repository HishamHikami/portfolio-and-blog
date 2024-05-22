from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import CaseStudy

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = "weekly"

    def items(self):
        return ["core:index"]

    def location(self, item):
        return reverse(item)
    
class CaseStudySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return CaseStudy.objects.filter(status="published")
    
    def lastmod(self, obj):
        return obj.date