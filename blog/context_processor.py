from blog.models import Category, Author

def default(request):
    categories = Category.objects.all()
    authors = Author.objects.all()

    return {
        'categories': categories,
        'authors': authors,
    }