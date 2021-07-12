from django.db import models
from datetime import time
# Create your models here.


class table(models.Model):
    table_number = models.IntegerField(default=1, unique=True)
    table_chairs = models.IntegerField(default=1,)

    def __str__(self):
        return f'Table ( {self.table_number} ), chairs: {self.table_chairs}'


class booking(models.Model):
    times = [
        (time(17, 00,), '5 PM'),
        (time(19, 00,), '7 PM'),
        (time(21, 00,), '9 PM'),
        (time(23, 00,), '11 PM'),
    ]
    booking_email = models.CharField(default="none", max_length=256)
    table_number = models.IntegerField(default='0')
    booked_for = models.CharField(max_length=30)
    booking_date = models.DateField()
    booking_time = models.TimeField(choices=times)
    phone_number = models.IntegerField(default='0000')

    def __str__(self):
        return f'{self.booking_email} has booked {self.table_number}'\
               f' for {str(self.booking_time)[:5]} on {self.booking_date}'


class menu(models.Model):
    types = [
        ('star', 'Starters'),
        ('main', 'Main course'),
        ('dess', 'Desserts'),
        ('adri', 'Alcoholic drinks'),
        ('ndri', 'Non-Alcholic drinks'),
    ]
    category = models.CharField(choices=types, max_length=64)
    course = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return f'{self.course}, {self.category}, {self.description}'
