from django.shortcuts import render
from .models import menu, table, booking
# Create your views here.


def get_home(request):
    return render(request, 'home/home.html')


def get_menu(request):
    menu_items = menu.objects.all()
    context = {
        'items': menu_items
    }
    return render(request, 'menu/menu.html', context)


def get_reservation(request):
    tables = table.objects.all()
    times = booking.times
    context = {
        'tables': tables,
        'times': times
    }
    return render(request, 'reservation/reservation.html', context)
