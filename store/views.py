from django.shortcuts import render
from .models import Categories, Product, Product_Item, Product_Item_Images,Customer, Order, OrderItem, ShippingAddress
from django.http import JsonResponse
# Create your views here.
def Home(request):
	CateList=Categories.objects.all()
	context={
	'CateList': CateList,
	}
	return render(request, 'home.html', context)
def AllCategories(request):
	CateList=Categories.objects.all()
	context={
	'CateList': CateList,
	}
	return render(request, 'categories.html', context)

def StoreAllProducts(request):
	pdtList=[]
	pdtCore = Product.objects.all()
	for pdtElement in pdtCore:
		pdt = Product_Item.objects.filter(Product=pdtElement)[0]
		name = pdtElement.name
		origin = pdtElement.origin_place
		pdtImage=Product_Item_Images.objects.filter(item=pdt)[0]
		pdtList += [[pdt, name, origin, pdtImage]]

	print(pdtImage.image.url)
	context={
	'pdtList': pdtList
	}

	return render(request, 'productsall.html', context)
def StoreProductsByCategory(request, pk):
	pdtList=[]
	CategoryObj = Categories.objects.get(id=pk)				#catch 404...better to make a custom 404 page instead
	pdtCore = Product.objects.filter(category=CategoryObj)
	for pdtElement in pdtCore:
		pdt = Product_Item.objects.filter(Product=pdtElement)[0]
		name = pdtElement.name
		origin = pdtElement.origin_place
		pdtImage=Product_Item_Images.objects.filter(item=pdt)[0]
		pdtList += [[pdt, name, origin, pdtImage]]

	print(pdtImage.image.url)
	context={
	'pdtList': pdtList
	}

	return render(request, 'productsall.html', context)



def Cart(request):
	pdtList=[]
	if request.user.is_authenticated:
		customer  = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		for item in items:
			pdtImage=Product_Item_Images.objects.filter(item=item.product)[0]
			pdtList += [[item, pdtImage]]
	else:
		pdtList=[]
		order = {'get_cart_total':0, 'get_cart_items':0}
	context={
	'pdtList': pdtList,
	'order': order,
	}
	return render(request, 'cart.html', context)

def CheckOut(request):
	pdtList=[]
	if request.user.is_authenticated:
		customer  = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		for item in items:
			pdtImage=Product_Item_Images.objects.filter(item=item.product)[0]
			pdtList += [[item, pdtImage]]
	else:
		pdtList=[]
		order = {'get_cart_total':0, 'get_cart_items':0}
	context={
	'pdtList': pdtList,
	'order': order,
	}
	return render(request, 'checkout.html', context)

def updateItem(request):
	return JsonResponse('Item was added.', safe=False)