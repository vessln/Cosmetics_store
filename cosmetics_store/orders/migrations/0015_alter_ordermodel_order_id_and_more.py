# Generated by Django 5.0.2 on 2024-04-06 15:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0014_alter_ordermodel_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='order_id',
            field=models.IntegerField(blank=True, default='0258142171', null=True),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='shipping_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.usershippingaddressmodel'),
        ),
    ]
