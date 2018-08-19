# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-22 16:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rome_app', '0005_auto_20171214_1533'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=254)),
                ('text', models.TextField()),
                ('pids', models.CharField(blank=True, help_text='Comma-separated list of pids for books or prints associated with this shop.', max_length=254, null=True)),
                ('people', models.ManyToManyField(blank=True, help_text='List of people associated with this Shop.', to='rome_app.Biography')),
            ],
        ),
    ]