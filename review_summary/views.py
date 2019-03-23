from django.shortcuts import render, get_object_or_404
# Create your views here.
from tablib import Dataset
from .models import Restaurant



def simple_upload(request):
    if request.method == 'POST':
        person_resource = RestaurantResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read())
        result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            person_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'core/simple_upload.html')

def restaurant_list(request):
    rest = Restaurant.objects.all()
    return render(request, 'restaurant/restaurants.html', {'restaurants': rest})

def restaurant_detail(request, id):
    rest = get_object_or_404(Restaurant, id=id)
    # rest = Restaurant.objects.all()
    return render(request, 'restaurant/restaurant_detail.html', {'restaurant': rest})