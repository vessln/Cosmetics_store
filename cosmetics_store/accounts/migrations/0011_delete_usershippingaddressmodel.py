# Generated by Django 5.0.2 on 2024-04-05 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_alter_usershippingaddressmodel_notes'),
        ('orders', '0010_alter_ordermodel_order_id_usershippingaddressmodel_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserShippingAddressModel',
        ),
    ]
