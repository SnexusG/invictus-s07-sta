# Generated by Django 3.2.9 on 2022-02-19 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bird_app', '0007_customuser_documents_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='stayAnonymous',
            field=models.BooleanField(default=False),
        ),
    ]
