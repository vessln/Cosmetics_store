# Generated by Django 5.0.4 on 2024-04-07 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0017_alter_ordermodel_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='order_id',
            field=models.IntegerField(blank=True, default='1310942171', null=True),
        ),
    ]
