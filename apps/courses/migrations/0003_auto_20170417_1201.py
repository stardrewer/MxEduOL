# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-17 12:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20170417_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='degree',
            field=models.CharField(choices=[('cj', '\u521d\u7ea7'), ('zj', '\u4e2d\u7ea7'), ('gj', '\u9ad8\u7ea7')], max_length=2, verbose_name='\u8bfe\u7a0b\u96be\u5ea6'),
        ),
        migrations.AlterField(
            model_name='course',
            name='desc',
            field=models.CharField(max_length=300, verbose_name='\u8bfe\u7a0b\u63cf\u8ff0'),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=50, verbose_name='\u8bfe\u7a0b\u540d'),
        ),
    ]
