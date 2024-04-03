# Generated by Django 5.0.2 on 2024-04-03 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_ordermodel_total_sum'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='completion_order_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='order_id',
            field=models.IntegerField(blank=True, default='1368312171', null=True),
        ),
    ]
