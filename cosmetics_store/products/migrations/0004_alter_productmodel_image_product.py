# Generated by Django 5.0.2 on 2024-03-19 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_productmodel_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='image_product',
            field=models.ImageField(upload_to='products_image/'),
        ),
    ]
