# Generated by Django 3.0.6 on 2021-08-19 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='qrcode',
            field=models.ImageField(blank=True, upload_to='Qrcode'),
        ),
    ]
