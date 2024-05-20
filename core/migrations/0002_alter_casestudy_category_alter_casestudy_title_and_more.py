# Generated by Django 5.0.4 on 2024-05-20 17:47

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casestudy',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.cscategory'),
        ),
        migrations.AlterField(
            model_name='casestudy',
            name='title',
            field=models.CharField(default='Company', max_length=40),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(default='john@email.com', max_length=40),
        ),
        migrations.AlterField(
            model_name='contact',
            name='full_name',
            field=models.CharField(default='John Doe', max_length=40),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(default='+1 234567890', max_length=40),
        ),
        migrations.AlterField(
            model_name='cscategory',
            name='description',
            field=models.CharField(default='Description', max_length=160),
        ),
        migrations.AlterField(
            model_name='cscategory',
            name='title',
            field=models.CharField(default=django.utils.timezone.now, max_length=40),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='faq',
            name='question',
            field=models.CharField(default='How helps?', max_length=100),
        ),
        migrations.AlterField(
            model_name='getquote',
            name='email',
            field=models.CharField(default='john@email.com', max_length=40),
        ),
        migrations.AlterField(
            model_name='seohomepage',
            name='description',
            field=models.CharField(default='SEO description', max_length=160),
        ),
        migrations.AlterField(
            model_name='seohomepage',
            name='title',
            field=models.CharField(default='SEO title', max_length=80),
        ),
        migrations.AlterField(
            model_name='technology',
            name='title',
            field=models.CharField(default='Logo', max_length=70),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='name',
            field=models.CharField(default='John Doe', max_length=40),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='profession',
            field=models.CharField(default='Engineer', max_length=40),
        ),
    ]
