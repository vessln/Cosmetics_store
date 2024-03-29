# Generated by Django 5.0.2 on 2024-03-19 13:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_product', models.CharField(max_length=30)),
                ('category', models.CharField(choices=[('Make-up', 'Make-up'), ('Skin care', 'Skin care'), ('Hair care', 'Hair care'), ('Personal Care', 'Personal Care')], max_length=25)),
                ('brand', models.CharField(max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=3)),
                ('image_product', models.ImageField(upload_to='')),
                ('description', models.TextField(max_length=500)),
                ('slug', models.SlugField()),
                ('manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
