# Generated by Django 5.0.2 on 2024-04-05 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_alter_ordermodel_order_id_usershippingaddressmodel_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='order_id',
            field=models.IntegerField(blank=True, default='7292032171', null=True),
        ),
    ]
