# Generated by Django 3.0.5 on 2020-09-17 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_paymentdetail_razpayorder_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentdetail',
            name='address',
            field=models.TextField(),
        ),
    ]
