# Generated by Django 4.2.4 on 2023-09-11 05:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flim', '0002_alter_booking_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='route',
            name='Duration',
        ),
    ]
