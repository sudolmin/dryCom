from django.urls import path
from . import api

urlpatterns = [
	# api urlpatterns
	path('category-api/', api.CateView, name="cate_api_view"),
]