# Generated by Django 3.2.5 on 2021-07-09 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_alter_booking_booking_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_time',
            field=models.TimeField(choices=[('17:00:00', '5 pm'), ('18:00:00', '6 pm'), ('19:00:00', '7 pm'), ('20:00:00', '8 pm'), ('21:00:00', '9 pm'), ('22:00:00', '10 pm'), ('23:00:00', '11 pm')]),
        ),
    ]
