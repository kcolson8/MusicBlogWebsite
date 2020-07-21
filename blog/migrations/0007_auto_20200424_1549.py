# Generated by Django 2.2.7 on 2020-04-24 22:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200418_2245'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='iFrameURL',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 24, 22, 49, 9, 637908, tzinfo=utc)),
        ),
    ]
