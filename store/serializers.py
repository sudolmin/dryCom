from rest_framework import serializers
from .models import *
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

class CartUpdateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Order
		fields = ['complete', 'reciept_id', 'get_cart_total', 'get_cart_items']

# class PaymentSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = PaymentDetail
# 		fields = ['get_reciept_id','shippingDict','get_order_id']
