# Generated by Django 2.2.7 on 2020-04-24 22:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200424_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 24, 22, 57, 54, 683772, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='iFrameURL',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
