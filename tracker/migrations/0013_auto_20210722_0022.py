# Generated by Django 3.2 on 2021-07-21 22:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0012_auto_20210721_2359'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='lastUpdate',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 22, 0, 22, 13, 997251)),
        ),
        migrations.AddField(
            model_name='leaguedata',
            name='streak',
            field=models.CharField(default='EEEEE', max_length=5),
        ),
    ]
