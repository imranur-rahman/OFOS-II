from django.contrib import admin
from .models import Customer, Area, Restaurant, Food, Rating, Cart, CartItem


admin.site.register(Customer)
admin.site.register(Area)
admin.site.register(Restaurant)
admin.site.register(Food)
admin.site.register(Rating)
admin.site.register(Cart)
admin.site.register(CartItem)
