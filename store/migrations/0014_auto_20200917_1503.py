# Generated by Django 3.0.5 on 2020-09-17 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_auto_20200917_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentdetail',
            name='status',
            field=models.CharField(default='None', max_length=20),
        ),
    ]
