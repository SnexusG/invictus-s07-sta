# Generated by Django 3.2.9 on 2022-02-19 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bird_app', '0008_post_stayanonymous'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='location',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='customuser',
            name='speciality',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
