# Generated by Django 2.0 on 2017-12-11 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20171211_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='votes_total',
            field=models.IntegerField(default=1),
        ),
    ]
