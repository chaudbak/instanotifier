# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 16:27
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rssnotification',
            options={'ordering': ['-published_parsed']},
        ),
    ]
