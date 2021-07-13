from django.shortcuts import render, get_object_or_404, redirect
from .models import menu, table, booking
from django.contrib.auth.models import User
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
    tables = table.objects.all()
    times = booking.times
    context = {
        'tables': tables,
        'times': times,
        'msg': msg,
    }
    return render(request, 'reservation/reservation.html',
                  context)


def get_thanks(request):
    get_form = request.POST
    fbooking_email = request.POST.get('booking_email')
    ftable_number = request.POST.get('table_number')
    fbooked_for = request.POST.get('booked_for')
    fbooking_date = request.POST.get('booking_date')
    fbooking_time = request.POST.get('booking_time')
    fphone_number = request.POST.get('phone_number')
    booking_msg = booking.objects.all()
    duplicate = 0
    for n, i in enumerate(booking_msg):
        check_one = str(i)[-25:]
        check_two = f'{ftable_number} for {fbooking_time} on {fbooking_date}'
        if check_one == check_two:
            duplicate += 1
    if duplicate == 0:
        booking.objects.create(
            booking_email=fbooking_email,
            table_number=ftable_number,
            booked_for=fbooked_for,
            booking_date=fbooking_date,
            booking_time=fbooking_time,
            phone_number=fphone_number,
        )
    else:
        print("Double booking")
        return get_reservation(request, msg='Table is already booked at\
                                             the given time, try another one.')
    context = {
        'get_form': get_form,
    }
    return render(request, 'thanks/thanks.html', context)


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