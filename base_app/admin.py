from django.contrib import admin
from .models import CategoryDish, Dish, Reservation, Event

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ['category', 'title', 'ingredients', 'price', 'image', 'description', 'dish_order', 'is_visibility', 'is_special']
    list_filter = ['category', 'dish_order', ]
    list_editable = ['price', 'dish_order']

@admin.register(CategoryDish)
class CategoryDish(admin.ModelAdmin):
    list_display = ['name', 'is_visibility', 'position']
    list_display_links = ['position', ]

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'date', 'time', 'count_people', 'message', 'is_processed']
    list_filter = ['date', 'time', ]
    list_editable = ['is_processed', ]

@admin.register(Event)
class EvetnAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'price', 'description', 'position',]
    list_filter = ['position',]
    list_editable = ['position', ]