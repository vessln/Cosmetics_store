# Generated by Django 5.0.2 on 2024-03-21 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_productmodel_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='description',
            field=models.TextField(max_length=800),
        ),
    ]
