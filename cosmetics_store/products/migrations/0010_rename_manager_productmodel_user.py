# Generated by Django 5.0.2 on 2024-04-05 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_productmodel_ingredients'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productmodel',
            old_name='manager',
            new_name='user',
        ),
    ]
