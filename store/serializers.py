from rest_framework import serializers
from .models import Categories, Product, 
					Product_Item, Product_Item_Images, 
					Customer, Order, 
					OrderItem, ShippingAddress
class PdtImgSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product_Item_Images
		fields = "__all__"


class PdtItemSerializer(serializers.ModelSerializer):
	images = PdtImgSerializer(many=True, read_only=True)
	class Meta:
		model = Product_Item
		fields = "__all__"
		fields+=images

class ProductSerializer(serializers.ModelSerializer):
	items = PdtItemSerializer(many=True, read_only=True)
	class Meta:
		model = Product
		fields = "__all__"
		fields+=items

class CategorySerializer(serializers.ModelSerializer):
	Products=ProductSerializer(many=True, read_only=True)
	class Meta:
		model = Categories
		fields = "__all__"
		fields+=Products

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = "__all__"