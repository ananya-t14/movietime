# Generated by Django 3.1.2 on 2020-10-23 18:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movietime', '0010_auto_20201023_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='SelectedDate',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='booking',
            name='SelectedTime',
            field=models.TimeField(),
        ),
    ]
