from django.contrib import admin
from . import models as _
from django.forms import TextInput, Textarea
from django.db import models

from nested_admin import NestedStackedInline, NestedTabularInline, NestedModelAdmin
# Register your models here.

class ImagesInline(NestedStackedInline):
	model=_.Product_Item_Images

class Product_ItemInline(NestedTabularInline):
	model=_.Product_Item
	formfield_overrides = {
    	models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':30})},
    }
	inlines=[ImagesInline]

class ProductAdmin(NestedModelAdmin):
	inlines=[Product_ItemInline]

class OrderItemAdmin(admin.ModelAdmin):
	list_display = ('product','order', 'quantity', 'date_added')

admin.site.register(_.Categories)
admin.site.register(_.Product, ProductAdmin)
admin.site.register(_.Customer)
admin.site.register(_.Order)
admin.site.register(_.OrderItem, OrderItemAdmin)
admin.site.register(_.ShippingAddress)