# Generated by Django 3.1.2 on 2020-10-23 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movietime', '0012_booking_moviename'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='cancelled',
            field=models.BooleanField(default=False),
        ),
    ]
