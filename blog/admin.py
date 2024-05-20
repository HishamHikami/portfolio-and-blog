from django.contrib import admin
from blog.models import Article, Author, Category

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['heading', 'slug', 'status', 'category', 'author']
    readonly_fields = ['slug']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    readonly_fields = ['slug']

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'user']

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)