# Generated by Django 4.0 on 2022-01-01 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_remove_total_price_total_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='total',
            name='name',
        ),
    ]