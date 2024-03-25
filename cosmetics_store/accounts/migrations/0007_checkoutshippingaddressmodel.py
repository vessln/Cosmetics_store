# Generated by Django 5.0.2 on 2024-03-22 17:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_storeusermodel_date_of_birth'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckoutShippingAddressModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=50)),
                ('street_address', models.CharField(max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]