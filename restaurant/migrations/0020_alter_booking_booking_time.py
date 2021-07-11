# Generated by Django 3.2.5 on 2021-07-11 21:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0019_delete_available_times'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_time',
            field=models.CharField(choices=[(datetime.time(17, 0), '5 PM'), (datetime.time(19, 0), '7 PM'), (datetime.time(21, 0), '9 PM'), (datetime.time(23, 0), '11 PM')], max_length=100),
        ),
    ]
