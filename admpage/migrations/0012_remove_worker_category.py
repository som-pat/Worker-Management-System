# Generated by Django 4.0.3 on 2022-03-29 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admpage', '0011_site_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worker',
            name='category',
        ),
    ]
