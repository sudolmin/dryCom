from django.shortcuts import render, get_object_or_404
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *

@api_view(['GET'])
def CateView(request):
	category = Categories.objects.all()
	serializer = CategorySerializer(category, many=True)
	return Response(serializer.data)
@api_view(['GET'])
def CartUpdate(request):
	if request.user.username == '': #AnonymousUser
		data={}
		data['get_cart_items'] = 0
		return Response(data)
	else:
		order = Order.objects.filter(customer=request.user.customer)
		serializer = CartUpdateSerializer(order, many=True)
		return Response(serializer.data)

# @api_view(['GET'])
# def RazorPayMent(request):
# 	payobj = PaymentDetail.objects.filter(customer=request.user.customer)
# 	serializer=PaymentSerializer(payobj, many=True)
# 	return Response(serializer.data)