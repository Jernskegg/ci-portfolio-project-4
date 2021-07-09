# Generated by Django 3.2.5 on 2021-07-09 12:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table',
            name='category',
        ),
        migrations.RemoveField(
            model_name='table',
            name='chairs',
        ),
        migrations.RemoveField(
            model_name='table',
            name='number',
        ),
        migrations.AddField(
            model_name='table',
            name='table_chairs',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='table',
            name='table_number',
            field=models.IntegerField(default=1, unique=True),
        ),
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Booked_for', models.CharField(max_length=30)),
                ('booking_date', models.DateField()),
                ('booking_time', models.TimeField(choices=[(1700, '5 pm'), (1800, '6 pm'), (1900, '7 pm'), (2000, '8 pm'), (2100, '9 pm'), (2200, '10 pm'), (2300, '11 pm')])),
                ('Bookholder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('book_table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.table')),
            ],
        ),
    ]
