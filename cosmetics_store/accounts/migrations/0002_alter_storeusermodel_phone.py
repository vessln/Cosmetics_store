# Generated by Django 5.0.2 on 2024-03-11 16:30

import cosmetics_store.accounts.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storeusermodel',
            name='phone',
            field=models.CharField(blank=True, max_length=10, null=True, validators=[cosmetics_store.accounts.validators.validator_check_valid_phone_number]),
        ),
    ]
