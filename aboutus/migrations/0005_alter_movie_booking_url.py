# Generated by Django 3.2 on 2021-11-07 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutus', '0004_movie_booking_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='booking_url',
            field=models.CharField(max_length=2083),
        ),
    ]
