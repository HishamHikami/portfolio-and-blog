from core.views import index
from django.urls import path
from blog.views import blog_detail, blog_list, tag_list

app_name = "blog"

urlpatterns = [
    path("blog/", blog_list, name='blog'),
    path("blog/<slug>", blog_detail, name='blog-detail'),
    path("blog/tag/<tag_slug>/", tag_list, name='tags'),
]