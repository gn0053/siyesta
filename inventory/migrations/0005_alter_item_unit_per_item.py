# Generated by Django 4.0.5 on 2024-01-12 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_item_unit_price_alter_item_unit_per_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='unit_per_item',
            field=models.FloatField(default=1),
        ),
    ]