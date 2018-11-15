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
urlpatterns += [
    path('city/<int:pk>/renew/', views.renew_city, name='renew-city'),
]
urlpatterns += [
    path('restaurant/create/', views.RestaurantCreate.as_view(), name='restaurant_create'),
    path('restaurant/<int:pk>/update/', views.RestaurantUpdate.as_view(), name='restaurant_update'),
    path('restaurant/<int:pk>/delete/', views.RestaurantDelete.as_view(), name='restaurant_delete'),
]
