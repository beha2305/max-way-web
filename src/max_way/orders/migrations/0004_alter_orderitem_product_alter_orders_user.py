# Generated by Django 5.0.3 on 2024-03-18 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_remove_orders_lat_remove_orders_long'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='orders',
            name='user',
            field=models.IntegerField(),
        ),
    ]