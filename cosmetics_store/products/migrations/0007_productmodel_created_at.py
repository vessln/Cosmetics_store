# Generated by Django 5.0.2 on 2024-03-27 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_productmodel_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
