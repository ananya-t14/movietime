# Generated by Django 3.1.2 on 2020-10-22 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movietime', '0008_auto_20201023_0114'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BookedSeats',
            new_name='Booking',
        ),
    ]