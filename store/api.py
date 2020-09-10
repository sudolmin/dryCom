from django.shortcuts import render, get_object_or_404
from .serializers import PdtImgSerializer, PdtItemSerializer,ProductSerializer, CategorySerializer,CategorySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Categories, Product, Product_Item, Product_Item_Images, Customer, Order, OrderItem, ShippingAddress

@api_view(['GET'])
def CateView(request):
	category = Categories.objects.all()
	serializer = CategorySerializer(category, many=True)
	# print(serializer.data)
	return Response(serializer.data)
