# Generated by Django 3.2.16 on 2022-11-13 11:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20221106_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='container',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 13, 11, 14, 30, 72476, tzinfo=utc), max_length=256),
        ),
    ]
