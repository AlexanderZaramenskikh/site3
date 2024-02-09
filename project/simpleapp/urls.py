from django.urls import path

from .views import ProductsList, ProductDetail , NewsDetail , NewsList

urlpatterns = [
   path('products/', ProductsList.as_view()),
   path('product/<int:pk>', ProductDetail.as_view()),
   path('news/', NewsList.as_view()),
   path('news/<int:pk>', NewsDetail.as_view()),
]