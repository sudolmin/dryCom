# Generated by Django 3.0.5 on 2020-09-12 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20200911_2313'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='image',
            field=models.ImageField(default='default-product.jpg', upload_to='Uploads'),
        ),
    ]
