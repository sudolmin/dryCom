# Generated by Django 3.0.5 on 2020-09-17 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_auto_20200917_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentdetail',
            name='paymentID',
            field=models.CharField(default='Unpaid', max_length=50),
        ),
        migrations.AlterField(
            model_name='paymentdetail',
            name='razpayorder_id',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='paymentdetail',
            name='status',
            field=models.CharField(default=None, max_length=20),
        ),
    ]
