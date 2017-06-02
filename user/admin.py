from django.contrib import admin
from .models import Customer, Area, Restaurant, Food, Rating


admin.site.register(Customer)
admin.site.register(Area)
admin.site.register(Restaurant)
admin.site.register(Food)
admin.site.register(Rating)
