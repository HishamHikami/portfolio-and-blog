# Generated by Django 5.0.4 on 2024-05-20 06:10

import blog.models
import django.db.models.deletion
import django_ckeditor_5.fields
import taggit.managers
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=60, null=True)),
                ('slug', models.SlugField(blank=True, max_length=80, null=True, unique=True)),
                ('image', models.ImageField(default='category.jpg', upload_to='category')),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='John Doe', max_length=100)),
                ('image', models.ImageField(default='author.jpg', upload_to='author')),
                ('description', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Authors',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(blank=True, max_length=80, null=True)),
                ('slug', models.SlugField(blank=True, max_length=80, null=True, unique=True)),
                ('cover', models.ImageField(upload_to=blog.models.blog_images)),
                ('body', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True)),
                ('excerpt', models.CharField(blank=True, max_length=450, null=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('in_review', 'In Review'), ('published', 'Published')], default='draft', max_length=20)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(blank=True, null=True)),
                ('meta_title', models.CharField(blank=True, max_length=60, null=True)),
                ('meta_description', models.CharField(blank=True, max_length=160, null=True)),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.author')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.category')),
            ],
            options={
                'verbose_name_plural': 'Articles',
            },
        ),
    ]