# Generated by Django 4.0.5 on 2024-01-12 10:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_alter_item_date_added'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='unit_price',
        ),
        migrations.AlterField(
            model_name='item',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 12, 10, 51, 37, 610668, tzinfo=utc)),
        ),
    ]