# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-04 11:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fir_artifacts', '0004_merge'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ArtifactWhitelistItem',
        ),
    ]
