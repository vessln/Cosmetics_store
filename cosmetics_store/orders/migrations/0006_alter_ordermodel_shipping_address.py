# Generated by Django 5.0.2 on 2024-03-26 13:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_remove_checkoutshippingaddressmodel_user_and_more'),
        ('orders', '0005_ordermodel_shipping_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='shipping_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.usershippingaddressmodel'),
        ),
    ]
