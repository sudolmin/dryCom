from django.contrib import admin
from .models import Categories ,Product, Product_Item, Product_Item_Images
from django.forms import TextInput, Textarea
from django.db import models

import nested_admin
# Register your models here.

class ImagesInline(nested_admin.NestedStackedInline):
	model=Product_Item_Images

class Product_ItemInline(nested_admin.NestedTabularInline):
	model=Product_Item
	formfield_overrides = {
    	models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':30})},
    }
	inlines=[ImagesInline]

class ProductAdmin(nested_admin.NestedModelAdmin):
	inlines=[Product_ItemInline]

admin.site.register(Categories)
admin.site.register(Product, ProductAdmin)