# Generated by Django 5.0.4 on 2024-05-22 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_casestudy_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='getquote',
            name='email',
            field=models.CharField(max_length=40),
        ),
    ]
