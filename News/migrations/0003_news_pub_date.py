# Generated by Django 3.0.1 on 2019-12-30 18:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0002_sportnews'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 30, 18, 9, 39, 25719, tzinfo=utc)),
        ),
    ]
