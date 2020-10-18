from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse
import json
from django.contrib.auth.decorators import login_required
from .forms import PaymentForm
# Create your views here.
def Home(request):
	CateList=Categories.objects.all()
	pdtList=[]
	pdtCore = Product.objects.all().order_by('-id')[:4]
	for pdtElement in pdtCore:
		pdt = Product_Item.objects.filter(Product=pdtElement)[0]
		name = pdtElement.name
		origin = pdtElement.origin_place
		if len(Product_Item_Images.objects.filter(item=pdt))==0:
			pdtImage='/static/images/default-product.jpg'
		else:
			pdtImage=Product_Item_Images.objects.filter(item=pdt)[0].image.url
		pdtList += [[pdt, name, origin, pdtImage]]

	context={
	'CateList': CateList,
	'LatestProduct':pdtList
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
		if len(Product_Item_Images.objects.filter(item=pdt))==0:
			pdtImage='/static/images/default-product.jpg'
		else:
			pdtImage=Product_Item_Images.objects.filter(item=pdt)[0].image.url
		pdtList += [[pdt, name, origin, pdtImage]]

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
		if len(Product_Item_Images.objects.filter(item=pdt))==0:
			pdtImage='/static/images/default-product.jpg'
		else:
			pdtImage=Product_Item_Images.objects.filter(item=pdt)[0].image.url
		pdtList += [[pdt, name, origin, pdtImage]]

	context={
	'pdtList': pdtList
	}

	return render(request, 'productsall.html', context)

@login_required
def Cart(request):
	pdtList=[]
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		for item in items:
			if len(Product_Item_Images.objects.filter(item=item.product))==0:
				pdtImage='/static/images/default-product.jpg'
			else:
				pdtImage=Product_Item_Images.objects.filter(item=item.product)[0].image.url
			pdtList += [[item, pdtImage]]
	else:
		pdtList=[]
		order = {'get_cart_total':0, 'get_cart_items':0}
	context={
	'pdtList': pdtList,
	'order': order,
	}
	return render(request, 'cart.html', context)

@login_required
def CheckOut(request):
	pdtList=[]
	if request.user.is_authenticated:
		customer  = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		for item in items:
			if len(Product_Item_Images.objects.filter(item=item.product))==0:
				pdtImage='/static/images/default-product.jpg'
			else:
				pdtImage=Product_Item_Images.objects.filter(item=item.product)[0].image.url
			pdtList += [[item, pdtImage]]
		if request.method == 'POST':
			raz_pay_form = PaymentForm(request.POST)
			if raz_pay_form.is_valid():
				if len(PaymentDetail.objects.filter(order=order))!=0:
					payObj=PaymentDetail.objects.get(order=order)
					payObj.delete()
				raz_obj=raz_pay_form.save(commit=False)
				print('\n\n',raz_obj,'\n\n')
				raz_obj.order=order
				raz_obj.save()
				return redirect("PaymentOrderId")
		else:
			raz_pay_form = PaymentForm()
	else:
		pdtList=[]
		order = {'get_cart_total':0, 'get_cart_items':0}
	context={
	'pdtList': pdtList,
	'order': order,
	"pay_form": raz_pay_form
	}
	return render(request, 'checkout.html', context)

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	customer = request.user.customer
	product = Product_Item.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)
	
	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
	
	if order.reciept_id==None:
		import random, string
		reciept = ''.join(random.choices(string.ascii_uppercase+string.ascii_lowercase+string.digits, k = 10))
		order.reciept_id=f'rId_{reciept}'
		order.save()
	
	if action =='add':
		orderItem.quantity += 1
	elif action == 'remove':
		orderItem.quantity -= 1

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added.', safe=False)

def PaymentOrderId(request):

# add a payment form in the checkout view 
# proccess all the required info from it and 
# render to payment.html embed the info to JS provided

	order=Order.objects.get(customer=request.user.customer, complete=False)
	payObj=PaymentDetail.objects.get(order=order)
	order_amount = int(order.get_cart_total)*100
	order_currency = 'INR'
	order_receipt = order.reciept_id
	customer_data = payObj.shippingDict  # OPTIONAL('notes')

	import razorpay

	KEY='rzp_test_9YfX33jkhilVYO'
	SECRET='eFUUQHk0jCoTNMvKUK7uFcrS'
	client = razorpay.Client(auth=(KEY, SECRET))
	client.set_app_details({"title" : "Django", "version" : "3.0.5"})

	order_dict=client.order.create({'amount':order_amount, 'currency':order_currency, 'receipt':order_receipt, 'notes':customer_data})

	payObj.razpayorder_id=order_dict['id']
	payObj.status=order_dict['status']
	payObj.save()

	print(payObj.razpayorder_id)
	print(order_dict)

	context={
		'order_id': payObj.razpayorder_id,
		'payObj':payObj,
		'amount':order_amount
	}
	return render(request, 'payment.html', context)

def SuccessPay(request, OrdID):
	payObj=PaymentDetail.objects.get(razpayorder_id=OrdID)
	if payObj.payondelivery==False and payObj.paymentID=='Unpaid':
		import razorpay

		KEY='rzp_test_9YfX33jkhilVYO'
		SECRET='eFUUQHk0jCoTNMvKUK7uFcrS'
		client = razorpay.Client(auth=(KEY, SECRET))
		client.set_app_details({"title" : "Django", "version" : "3.0.5"})

		for i in range(len(client.order.payments(OrdID)['items'])):
			if client.order.payments(OrdID)['items'][i]['status']=='captured':
				payObj.status=client.order.fetch(OrdID)['status']
				payObj.paymentID=client.order.payments(OrdID)['items'][i]['id']
				payObj.save()

	items=payObj.order.get_cart_items
	amount=payObj.order.get_cart_total
	print(payObj.order.complete)
	payObj.order.complete=True
	payObj.order.save()
	print(payObj.order.complete)
	context={
		'order_id': OrdID,
		'payObj':payObj,
		'amount':amount,
		'items':items
	}
	return render(request, 'success.html', context)

# def CashOnDelivery(request, OrdID):
# 	payObj=PaymentDetail.objects.get(razpayorder_id=OrdID)
# 	amount=payObj.order.get_cart_total
# 	payObj.payondelivery=True

def Filter(request):
	
	return render(request, 'home.html', context)