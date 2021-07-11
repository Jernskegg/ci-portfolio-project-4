# Generated by Django 3.2.5 on 2021-07-11 20:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0016_auto_20210711_2204'),
    ]

    operations = [
        migrations.DeleteModel(
            name='open_time',
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_time',
            field=models.TimeField(choices=[(datetime.time(17, 0), '5 PM'), (datetime.time(19, 0), '7 PM'), (datetime.time(21, 0), '9 PM'), (datetime.time(23, 0), '11 PM')]),
        ),
    ]
