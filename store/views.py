from django.shortcuts import render
from django.views import generic

from django.http import HttpResponse
from store.models import City, Restaurant

from store.forms import RenewCityForm
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


import datetime

def index(request):
    citys = City.objects.all()
    restaurants = Restaurant.objects.all()
    context = {'citys': citys, 'restaurants': restaurants}
    return render(request, 'store/index.html', context)

@permission_required('store.can_mark_returned')
def renew_city(request, pk):
    city_instance = get_object_or_404(City, pk=pk)

    if request.method == 'POST':
        city_renewal_form = RenewCityForm(request.POST)
        if city_renewal_form.is_valid():
            city_instance.due_back = city_renewal_form.cleaned_data['renewal_date']
            city_instance.save()
            return HttpResponseRedirect(reverse('all-borrowed') )
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        city_renewal_form = RenewCityForm(initial={'renewal_date': proposed_renewal_date})

    context = {
        'form': city_renewal_form,
        'city_instance': city_instance,
    }

    return render(request, 'store/renew_city.html', context)


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


class RestaurantCreate(CreateView):
    model = Restaurant
    fields = '__all__'
    initial = {'date_of_death': '05/01/2018'}

class RestaurantUpdate(UpdateView):
    model = Restaurant
    fields = ['res_name', 'res_address', 'res_description']

class RestaurantDelete(DeleteView):
    model = Restaurant
    success_url = reverse_lazy('restaurants')


