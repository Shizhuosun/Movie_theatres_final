# Generated by Django 3.2 on 2021-11-08 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutus', '0005_alter_movie_booking_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='image',
            field=models.CharField(default='abc', max_length=2083),
        ),
    ]
