# Generated by Django 3.0 on 2019-12-24 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MarketPlaceApp', '0008_auto_20191224_0739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img_url',
            field=models.ImageField(upload_to=''),
        ),
    ]