# Generated by Django 3.1.2 on 2020-10-23 10:41

from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movietime', '0009_auto_20201023_0117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nowplaying',
            name='movie',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='seatnumber',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='time',
        ),
        migrations.AddField(
            model_name='booking',
            name='BookingTime',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='SelectedTime',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='movieid',
            field=models.IntegerField(default=0, verbose_name='Movie ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='booking',
            name='user',
            field=models.ManyToManyField(related_name='seat_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='MovieDatabase',
        ),
        migrations.DeleteModel(
            name='NowPlaying',
        ),
    ]
