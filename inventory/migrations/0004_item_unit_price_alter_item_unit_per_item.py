# Generated by Django 4.0.5 on 2024-01-12 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_item_item_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='unit_price',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='item',
            name='unit_per_item',
            field=models.IntegerField(default=1),
        ),
    ]
