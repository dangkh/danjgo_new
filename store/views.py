from django.shortcuts import render
from django.views import generic

from django.http import HttpResponse
from store.models import City, Restaurant


def index(request):
    citys = City.objects.all()
    restaurants = Restaurant.objects.all()
    context = {'citys': citys, 'restaurants': restaurants}
    return render(request, 'store/index.html', context)

class CityListView(generic.ListView):
    model = City
    template_name ='store/listcitys.html'

class CityDetailView(generic.DetailView):
    model = City
    template_name ='store/detailcity.html'

class RestaurantListView(generic.ListView):
    model = Restaurant
    template_name ='store/listrestaurants.html'

class RestaurantDetailView(generic.DetailView):
    model = Restaurant
    template_name ='store/detailrestaurant.html'


