# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-05 07:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20190805_1022'),
    ]

    operations = [
        migrations.CreateModel(
            name='LunImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=150, verbose_name='图片url')),
                ('detail_url', models.CharField(max_length=150, verbose_name='详情url')),
            ],
            options={
                'db_table': 'lunimage',
            },
        ),
    ]
