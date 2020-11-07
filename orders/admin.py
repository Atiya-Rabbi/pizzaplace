from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Regular)
admin.site.register(Sicilian)
admin.site.register(Toppings)
admin.site.register(Subs)
admin.site.register(Pasta)
admin.site.register(Salads)
admin.site.register(Dinner)
admin.site.register(Order)
admin.site.register(ConfirmedOrders)