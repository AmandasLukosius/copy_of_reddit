# Generated by Django 2.0 on 2017-12-11 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20171211_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='votes_total',
            field=models.IntegerField(default=0),
        ),
    ]
