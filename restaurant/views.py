from django.shortcuts import render, get_object_or_404
from .models import menu, booking
# from django.contrib.auth.models import User
from .forms import BookingForm
from datetime import date
# Create your views here


def get_home(request):
    return render(request, 'home/home.html')


def get_menu(request):
    menu_items = menu.objects.all()
    context = {
        'items': menu_items
    }
    return render(request, 'menu/menu.html', context)


def get_reservation(request, msg=""):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return get_thanks(request, form.cleaned_data)
    if request.user.is_authenticated:
        form = BookingForm(
            initial={'booking_email': request.user.email,
                     'booked_for':
                     f'{request.user.first_name} {request.user.last_name}',
                     'booking_date': date.today()
                     }
        )
    else:
        form = BookingForm(
            initial={
                     }
        )
    context = {
        'form': form,
        'msg': msg,
    }
    return render(request, 'reservation/reservation.html', context)


def get_thanks(request, ty_message):
    print(ty_message)
    return render(request, 'thanks/thanks.html', {'get_form': ty_message})


def get_myaccount(request):
    username = 'anon'
    if request.user.is_authenticated:
        username = request.user.email
    filter_me = booking.objects.all()
    bookings = filter_me.filter(booking_email=username)
    context = {
        'bookings': bookings,
    }
    return render(request, 'my_account/my_account.html', context)


def unbook(request, item_id):
    item = get_object_or_404(booking, id=item_id)
    item.delete()
    return get_myaccount(request)
