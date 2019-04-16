from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.models import User

# Create your views here.
from tablib import Dataset
from .models import Restaurant, Review
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms

from django.http import HttpResponseRedirect
from .forms import RegisterForm



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

def index_page(request):
    return render(request, 'restaurant/intro.html', {})

def get_restaurants(request):
    query = request.GET.get('search')
    locality = request.GET.get('locality')
    cost = request.GET.get('costForTwo')
    cuisine = request.GET.get('cuisine')

    # , restaurantLocation=locality
    # if locality == None:
    #     rest = Restaurant.objects.filter(restaurantCity__icontains=query, )
    # elif cost == None:

    # elif cuisine = None:

    # else:
    #     rest = Restaurant.objects.filter(restaurantCity__icontains=query, restaurantLocation__icontains=locality)

    rest = Restaurant.objects.filter(restaurantCity__icontains=query or '', restaurantLocation__icontains=locality or '', 
                                     restaurantCostForTwo__gte=cost or 9999, restaurantCusine__icontains=cuisine or '')

    paginator = Paginator(rest, 25) # Show 25 contacts per page
    page = request.GET.get('page')
    rest = paginator.get_page(page)
    return render(request, 'restaurant/restaurant.html', {'restaurants': rest, 'query': query})

def restaurant_list(request):
    rest = Restaurant.objects.all()
    return render(request, 'restaurant/restaurants.html', {'restaurants': rest})

def restaurant_detail(request, id):
    rest = get_object_or_404(Restaurant, id=id)
    review = Review.objects.filter(rest_id=id)
    # rest = Restaurant.objects.all()
    return render(request, 'restaurant/restaurant_detail.html', {'restaurant': rest, 'reviews': review})

# def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email =  userObj['email']
            password =  userObj['password']
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username = username, password = password)
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                raise forms.ValidationError('Looks like a username with that email or password already exists')
    else:
        form = UserRegistrationForm()
    return render(request, 'mysite/register.html', {'form' : form})

def user_register(request):
    # if this is a POST request we need to process the form data
    template = 'restaurant/signup.html'
    
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, template, {
                    'form': form, 
                    'error_message': 'Username already exists.'
                })
            elif User.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form': form, 
                    'error_message': 'Email already exists.'
                })
            elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
                return render(request, template, {
                    'form': form, 
                    'error_message': 'Passwords do not match.'
                })
            else:
                # Create the user: 
                user = User.objects.create_user(
                    form.cleaned_data['username'], 
                    form.cleaned_data['email'], 
                    form.cleaned_data['password']
                )
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.phone_number = form.cleaned_data['phone_number']
                user.save()
                
                # Login the user
                login(request, user)
                
                # redirect to accounts page:
                return HttpResponseRedirect('/')

   # No post data availabe, let's just show the page.
    else:
        form = RegisterForm()

    return render(request, template, {'form': form})