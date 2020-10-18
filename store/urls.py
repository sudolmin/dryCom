from django.urls import path
from . import api, views

urlpatterns = [
	path('', views.Home, name="home"),
	path('cart/', views.Cart, name="Cart"),
	path('checkout/', views.CheckOut, name="CheckOut"),
	path('store/', views.StoreAllProducts, name="store"),
	path('store/category/all/', views.AllCategories, name="category-all"),
	path('store/category/<str:pk>/', views.StoreProductsByCategory, name="CateID"),
	path('updateItem/', views.updateItem, name="updateItem"),
	path('payment/', views.PaymentOrderId, name="PaymentOrderId"),
	path('payment/<str:OrdID>/success/', views.SuccessPay, name="SuccessPay" ),
	# path('payment/cod/<str:OrdID>/', views.CashOnDelivery, name='Cash-On-Delivery'),
	path('store/filter/', views.Filter, name="filter"),
	
	# api urlpatterns
	path('category-api/', api.CateView, name="cate_api_view"),
	path('cart-api/', api.CartUpdate, name="cart_api_view"),
	# path('pay-api/', api.RazorPayMent, name="pay"),
]