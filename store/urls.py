from django.urls import path
from . import api, views

urlpatterns = [
	path('', views.Home, name="home"),
	path('cart/', views.Cart, name="Cart"),
	path('checkout/', views.CheckOut, name="CheckOut"),
	path('store/', views.StoreAllProducts, name="store"),
	path('store/category/all/', views.AllCategories, name="category-all"),
	path('store/category/<str:pk>/', views.StoreProductsByCategory, name="CateID"),

	# api urlpatterns
	path('category-api/', api.CateView, name="cate_api_view"),
]