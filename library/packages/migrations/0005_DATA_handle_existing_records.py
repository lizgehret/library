# ----------------------------------------------------------------------------
# Copyright (c) 2018-2022, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from django.db import migrations


def update_existing_package_build_records(apps, schema_editor):
    Epoch = apps.get_model('packages', 'Epoch')
    PackageBuild = apps.get_model('packages', 'PackageBuild')

    epoch, _ = Epoch.objects.get_or_create(
        name='pre_package_integration',
        is_dev=False,
        include_in_ci=False,
    )

    for record in PackageBuild.objects.all():
        record.epoch = epoch
        record.save()


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0004_integration_first_pass'),
    ]

    operations = [
        migrations.RunPython(update_existing_package_build_records),
    ]
