from django.urls import path
from . import api, views

urlpatterns = [
	path('', views.Store, name="Store"),
	path('cart/', views.Cart, name="Cart"),
	path('checkout/', views.CheckOut, name="CheckOut"),
	# api urlpatterns
	path('category-api/', api.CateView, name="cate_api_view"),
]