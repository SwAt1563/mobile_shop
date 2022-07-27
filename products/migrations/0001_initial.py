# Generated by Django 4.0.6 on 2022-07-27 12:46

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('categories', models.ManyToManyField(blank=True, to='products.category')),
            ],
        ),
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('size', models.IntegerField()),
                ('price', models.FloatField()),
                ('about', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100, null=True), size=10)),
                ('mobile_image', models.ImageField(blank=True, null=True, upload_to='mobiles_images/')),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='products.category')),
            ],
        ),
    ]
