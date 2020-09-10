from django.contrib import admin
from .models import Categories ,Product, Product_Item, Product_Item_Images
from django.forms import TextInput, Textarea
from django.db import models

from nested_admin import NestedStackedInline, NestedTabularInline, NestedModelAdmin
# Register your models here.

class ImagesInline(NestedStackedInline):
	model=Product_Item_Images

class Product_ItemInline(NestedTabularInline):
	model=Product_Item
	formfield_overrides = {
    	models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':30})},
    }
	inlines=[ImagesInline]

class ProductAdmin(NestedModelAdmin):
	inlines=[Product_ItemInline]

admin.site.register(Categories)
admin.site.register(Product, ProductAdmin)