# Generated by Django 3.2.5 on 2021-07-09 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0013_alter_booking_booking_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('star', 'Starters'), ('main', 'Main course'), ('dess', 'Desserts'), ('adri', 'Alcoholic drinks'), ('ndri', 'Non-Alcholic drinks')], max_length=64)),
                ('Course', models.CharField(max_length=30)),
                ('description', models.TextField()),
            ],
        ),
    ]
