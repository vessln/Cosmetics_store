# Generated by Django 5.0.4 on 2024-04-11 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_articlemodel_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlemodel',
            name='article_image',
            field=models.URLField(max_length=1000),
        ),
    ]