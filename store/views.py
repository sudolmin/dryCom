from django.shortcuts import render
from .models import Categories, Product, Product_Item, Product_Item_Images
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
	return render(request, 'cart.html')

def CheckOut(request):
	return render(request, 'checkout.html')