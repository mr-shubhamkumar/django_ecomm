# Generated by Django 4.2.7 on 2023-11-27 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discription',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='discounted_price',
            field=models.FloatField(),
        ),
    ]