# Generated by Django 3.2.5 on 2021-07-19 21:34

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import restaurant.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restaurant', '0028_alter_booking_booking_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_time',
            field=models.TimeField(choices=[(datetime.time(17, 0), '5 PM'), (datetime.time(19, 0), '7 PM'), (datetime.time(21, 0), '9 PM'), (datetime.time(23, 0), '11 PM')], default=[(datetime.time(17, 0), '5 PM'), (datetime.time(19, 0), '7 PM'), (datetime.time(21, 0), '9 PM'), (datetime.time(23, 0), '11 PM')]),
        ),
        migrations.AlterField(
            model_name='booking',
            name='table_number',
            field=models.ForeignKey(default=restaurant.models.table, on_delete=django.db.models.deletion.CASCADE, to='restaurant.table'),
        ),
        migrations.CreateModel(
            name='user_number',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, default='0123456789', max_length=30)),
                ('user_phone_number', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
