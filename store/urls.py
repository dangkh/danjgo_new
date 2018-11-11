from django.urls import path
from . import views

app_name = 'store'
urlpatterns = [
    path('', views.index, name='index'),
    path('city/', views.CityListView.as_view(), name='citys'),
    path('city/<int:pk>', views.CityDetailView.as_view(), name='city_detail'),
    path('restaurant/', views.RestaurantListView.as_view(), name='restaurants'),
    path('restaurant/<int:pk>', views.RestaurantDetailView.as_view(), name='restaurant_detail'),
]
