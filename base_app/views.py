from django.shortcuts import render, redirect
from .models import Dish, CategoryDish, Reservation, Event
from .form import FormReservation

def base_app_view(request):
    if request.method == 'POST':
        form = FormReservation(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    form_reservation = FormReservation()
    dishes = Dish.objects.filter(is_visibility=True, is_special=False).order_by('dish_order')
    categories = CategoryDish.objects.filter(is_visibility=True).order_by('position')
    special = Dish.objects.filter(is_visibility=True, is_special=True).order_by('dish_order')
    evets = Event.objects.filter().order_by('position')
    return render(request, 'base_app.html', context={
        'dishes': dishes,
        'categories': categories,
        'special': special,
        'form_reservation': form_reservation,
        'events': evets,
    })



