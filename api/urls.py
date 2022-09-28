from django.urls import path ,include
from api import views
urlpatterns = [
 	path('ProductsList',views.ProductsList.as_view(),name='ProductsList'),
    path('ProductsDetail/<int:id>',views.ProductDetail.as_view()),
]