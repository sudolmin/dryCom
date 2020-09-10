from rest_framework import serializers
from .models import Categories, Product, Product_Item, Product_Item_Images, Customer, Order, OrderItem, ShippingAddress
class PdtImgSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product_Item_Images
		fields = ['image']


class PdtItemSerializer(serializers.ModelSerializer):
	images = PdtImgSerializer(many=True)
	class Meta:
		model = Product_Item
		fields = ['price','discount','weight','about',
		'howtouse','benefits','ingredient', 'images']

class ProductSerializer(serializers.ModelSerializer):
	items = PdtItemSerializer(many=True)
	class Meta:
		model = Product
		fields = ['name', 'origin_place','items']

class CategorySerializer(serializers.ModelSerializer):
	Products=ProductSerializer(many=True)
	class Meta:
		model = Categories
		fields = ['title', 'Products']