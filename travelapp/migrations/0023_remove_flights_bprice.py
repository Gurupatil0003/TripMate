# Generated by Django 2.2.11 on 2020-03-30 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0022_flights_seats'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flights',
            name='bprice',
        ),
    ]
