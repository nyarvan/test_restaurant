from django.shortcuts import render, redirect
from base_app.models import Reservation
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator

def is_manager(user):
    return user.groups.filter(name='manager').exists()


@login_required(login_url='/login/')
@user_passes_test(is_manager)
def reservations_list(request):
    reservation = Reservation.objects.filter(is_processed=False).order_by('-date')

    paginator = Paginator(reservation, 5)
    page = request.GET.get('page')

    reservation = paginator.get_page(page)
    return render(request, 'reservation_list.html', context={'reg_list': reservation})

@login_required(login_url='/login/')
@user_passes_test(is_manager)
def update_reservation(request, pk):
    Reservation.objects.filter(pk=pk).update(is_processed=True)
    return redirect('reservations/')