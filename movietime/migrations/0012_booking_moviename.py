# Generated by Django 3.1.2 on 2020-10-23 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movietime', '0011_auto_20201023_2356'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='moviename',
            field=models.CharField(default='Movie', max_length=100),
        ),
    ]
