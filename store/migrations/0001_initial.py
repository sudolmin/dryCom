# Generated by Django 3.0.5 on 2020-09-10 09:48

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('origin_place', models.CharField(max_length=250)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Categories')),
            ],
        ),
        migrations.CreateModel(
            name='Product_Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default=0.0, help_text='Price per item', validators=[django.core.validators.MinValueValidator(0)], verbose_name='Price')),
                ('discount', models.FloatField(default=0, help_text='Discount offer', validators=[django.core.validators.MinValueValidator(0)], verbose_name='Discount')),
                ('weight', models.CharField(max_length=20)),
                ('about', models.TextField(blank=True, help_text='Describe the product.', null=True, verbose_name='About The Item')),
                ('howtouse', models.TextField(blank=True, help_text='Write how to consume/use the item.', null=True, verbose_name='How to use')),
                ('benefits', models.TextField(blank=True, help_text='Write how will the product benefit them.', null=True, verbose_name='Benefits')),
                ('ingredient', models.TextField(blank=True, help_text='Write the things that are included in the pakaging.', null=True, verbose_name='Ingredients')),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Product_Item_Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default-product.jpg', upload_to='ProfilePics')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Product_Item')),
            ],
        ),
    ]
