# Generated by Django 2.1.7 on 2019-03-22 20:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review_summary', '0007_person'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='restaurantMenuURL',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='restaurantPhotosURL',
        ),
    ]
