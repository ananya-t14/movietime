# Generated by Django 3.1.2 on 2020-10-22 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movietime', '0002_user_phonenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phonenumber',
            field=models.CharField(max_length=20),
        ),
    ]
