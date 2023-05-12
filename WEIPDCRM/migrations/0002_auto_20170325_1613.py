# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-25 15:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WEIPDCRM', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='qq_group_name',
            field=models.CharField(max_length=128, null=True, verbose_name='QQ Group Name'),
        ),
        migrations.AddField(
            model_name='setting',
            name='qq_group_number',
            field=models.FloatField(help_text='Show QQ Group link in mobile package info page', null=True, verbose_name='QQ Group Number'),
        ),
    ]
