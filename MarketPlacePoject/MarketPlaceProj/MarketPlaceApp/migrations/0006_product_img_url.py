# Generated by Django 3.0 on 2019-12-24 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MarketPlaceApp', '0005_remove_product_img_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='img_url',
            field=models.ImageField(default='default.jpg', upload_to='gallery'),
            preserve_default=False,
        ),
    ]