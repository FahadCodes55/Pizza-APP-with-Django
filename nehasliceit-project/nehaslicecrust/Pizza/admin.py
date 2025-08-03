from django.contrib import admin
from .models import Pizza, OrderPizza


# Register your models here.

class PizzaAdmin(admin.ModelAdmin):
    list_display = ('name',)

class OrderPizzaAdmin(admin.ModelAdmin):
    list_display = ('user',)

admin.site.register(Pizza, PizzaAdmin)
admin.site.register(OrderPizza, OrderPizzaAdmin)

# Change admin site headers
admin.site.site_header = "Pizza App Administration"
admin.site.site_title = "Pizza App Admin"
admin.site.index_title = "Welcome to Pizza App Administration"
