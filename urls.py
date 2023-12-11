from django.urls import path

from . import views
urlpatterns = [
	path('',views.homepage),
	path("products/",views.products),
	path("productdetails<int:product_id>",views.product_details),
]