from core.views import index
from django.urls import path
from blog.views import blog_detail, blog_list, tag_list
from django.contrib.sitemaps.views import sitemap
from .sitemap import ArticleSitemap

app_name = "blog"

sitemaps = {
    'posts': ArticleSitemap
}

urlpatterns = [
    path("blog/", blog_list, name='blog'),
    path("blog/<slug>", blog_detail, name='blog-detail'),
    path("blog/tag/<tag_slug>/", tag_list, name='tags'),
    path(
        "blog-sitemap.xml",
        sitemap,
        {
            'sitemaps': sitemaps
        },
        name = 'django.contrib.sitemaps.views.sitemap'
    ),
]