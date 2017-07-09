from django.contrib import admin
from .models import Customer, Area, Restaurant, Food, Rating, Cart, CartItem, Employee, NewOrders, CompletedOrders


admin.site.register(Customer)
admin.site.register(Area)
admin.site.register(Restaurant)
admin.site.register(Food)
admin.site.register(Rating)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Employee)
admin.site.register(NewOrders)
admin.site.register(CompletedOrders)