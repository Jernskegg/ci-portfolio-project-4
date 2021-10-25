from django import forms
from .models import booking
from django.contrib.auth.models import User


class BookingForm(forms.ModelForm):
    class Meta:
        model = booking
        fields = [
            'booking_email',
            'table_number',
            'booked_for',
            'booking_date',
            'booking_time',
            'phone_number',
        ]
        labels = {
            'phone_number': 'Phone number (Optional)',
        }


class AccountForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'email',
            'first_name',
            'last_name',
        ]
