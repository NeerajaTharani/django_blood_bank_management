# Generated by Django 3.0.5 on 2024-04-16 06:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0002_auto_20240416_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blooddonate',
            name='after_donate_blood',
            field=models.DateField(default=datetime.datetime(2024, 4, 16, 11, 46, 24, 392240)),
        ),
    ]