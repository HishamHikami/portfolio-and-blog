from django.shortcuts import get_object_or_404, render
from blog.models import Article
from taggit.models import Tag

# Create your views here.

def blog_detail(request, slug):
    article = Article.objects.get(slug=slug)
    articles = Article.objects.filter(status="published")

    context = {
        "article": article,
        "articles": articles,
    }
    
    return render(request, 'blog/blog-detail.html', context)

def blog_list(request):
    articles = Article.objects.filter(status="published").order_by("-date")

    context = {
        "articles": articles
    }

    return render(request, 'blog/blog-list.html', context)

def tag_list(request, tag_slug=None):
    articles = Article.objects.filter(status="published").order_by("-date")

    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        articles = articles.filter(tags__in=[tag])

    context = {
        "articles": articles,
        "tag": tag,
    }

    return render(request, 'blog/tag.html', context)