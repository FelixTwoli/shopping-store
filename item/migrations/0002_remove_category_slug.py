# Generated by Django 4.2.4 on 2023-08-20 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
    ]
