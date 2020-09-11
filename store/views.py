from django.shortcuts import render

# Create your views here.
def Store(request):
	return render(request, 'home.html')

def Cart(request):
	return render(request, 'cart.html')

def CheckOut(request):
	return render(request, 'checkout.html')