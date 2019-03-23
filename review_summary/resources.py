from import_export import resources
from .models import Restaurant
from .models import Person

class RestaurantResource(resources.ModelResource):
    class Meta:
        model = Restaurant

class PersonResource(resources.ModelResource):
    class Meta:
        model = Person