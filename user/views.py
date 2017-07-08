from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.db.models import Q
from .forms import UserLoginForm, UserRegistrationForm
from .models import Customer, Area, Restaurant, Food
from django.contrib.sessions.models import Session


def logOut(request):
    logout(request)
    return render(request, 'user/logout.html')


def add_to_cart(request, food_id):

    print('in add to cart')
    query = food_id
    print(request.session['username'])
    print(food_id)

    queryset_list = {}
    if query:
        '''queryset_list = Restaurant.objects.filter(Q(name__icontains=query) |
                                                  Q(area__name__contains=query))'''
        print('add to cart is' + query)

    context = {
        'object_list': queryset_list,
    }

    #return render(request, 'user/foods.html', context)
    return redirect('user:foods')


class IndexView(generic.ListView):
    template_name = 'user/index.html'
    # context_object_name =

    def get_queryset(self):
        return Customer.objects.all()


class UserLoginFormView(View):
    form_class = UserLoginForm
    template_name = 'user/login.html'

    # display blank line
    def get(self, request):
        form = self.form_class(None)
        # print("get", form)
        return render(request, self.template_name, {
            'form': form,
            'error': '',
        })

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        username = request.POST.get("username")
        password = request.POST.get("password")
        #username = form.cleaned_data['username']
        #password = form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        print(username, password)

        if user is not None:
            if user.is_active:
                login(request, user)
                request.session['username'] = username
                return redirect('user:index')
        else:
            error = 'Wrong username password combination!'
            return render(request, self.template_name, {
                'form': form,
                'error': error,
            })


class UserRegistrationFormView(View):
    form_class = UserRegistrationForm
    template_name = 'user/register.html'

    # display blank line
    def get(self, request):
        form = self.form_class(None)
        # print("get", form)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):

        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            # cleaned (neutralized) data
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            user.set_password(password)

            user.save()

            # print("register: "+first_name+last_name+username+email+password)

            # returns user object if credentials are correct
            user = authenticate(request, first_name=first_name, last_name=last_name, username=username, password=password, email=email)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('user:index')

        return render(request, self.template_name, {'form': form})


class RestaurantListView(View):

    def get(self, request):

        query = request.GET.get("q")
        queryset_list = {}
        if query:
            queryset_list = Restaurant.objects.filter(Q(name__icontains=query) |
                                                      Q(area__name__contains=query))

        context = {
            'object_list': queryset_list,
        }

        return render(request, 'user/restaurants.html', context)


class RestaurantView(View):

    def get(self, request, id):

        queryset = Food.objects.filter(restaurant__pk=id)
        context = {
            'object_list': queryset,
        }
        return render(request, 'user/restaurant.html', context)


class AllFoodView(View):

    def get(self, request):

        queryset = Food.objects.all()
        context = {
            'object_list': queryset,
            'which_to_add': "",
        }
        request.session['food_to_be_added'] = '0'
        return render(request, 'user/foods.html', context)


class CheckoutView(View):

    def get(self, request):

        queryset = {}
        context = {
            'object_list': queryset,
        }
        return render(request, 'user/checkout.html', context)