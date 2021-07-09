from django.db import models
from django.contrib.auth.models import User
from datetime import time
# Create your models here.


class table(models.Model):
    table_number = models.IntegerField(default=1, unique=True)
    table_chairs = models.IntegerField(default=1,)

    def __str__(self):
        return f'Table ( {self.table_number} ), chairs: {self.table_chairs}'


class booking(models.Model):
    times = []
    open_time = 5
    close_time = 12
    book_duration = 2
    open_close = range(open_time, close_time)

    for i in open_close[0::book_duration]:
        times.append((time(i+12, 00,), f'{i} PM'))

    Bookholder = models.ForeignKey(User, on_delete=models.CASCADE)
    book_table = models.ForeignKey(table, on_delete=models.CASCADE)
    Booked_for = models.CharField(max_length=30)
    booking_date = models.DateField()
    booking_time = models.TimeField(choices=times)

    def __str__(self):
        return f'{self.Bookholder} has booked {self.book_table} for {str(self.booking_time)[:5]} on {self.booking_date}'
