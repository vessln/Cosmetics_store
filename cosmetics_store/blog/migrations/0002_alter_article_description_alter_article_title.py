# Generated by Django 5.0.2 on 2024-03-04 17:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='description',
            field=models.TextField(max_length=3000, validators=[django.core.validators.MinLengthValidator(20)]),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3)]),
        ),
    ]
