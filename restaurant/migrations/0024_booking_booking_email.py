# Generated by Django 3.2.5 on 2021-07-12 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0023_auto_20210712_0412'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='booking_email',
            field=models.CharField(default='none', max_length=256),
        ),
    ]
