# Generated by Django 5.0.2 on 2024-07-17 04:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pythonapp', '0004_model3'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='model3',
            name='price',
        ),
        migrations.RemoveField(
            model_name='model3',
            name='quantity',
        ),
    ]
