# ----------------------------------------------------------------------------
# Copyright (c) 2018-2022, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

# Generated by Django 3.2.9 on 2021-11-12 22:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0009_auto_20210908_1525'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='distrobuild',
            unique_together={('distro', 'version', 'epoch')},
        ),
    ]