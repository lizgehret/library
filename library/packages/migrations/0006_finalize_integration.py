# Generated by Django 3.2.6 on 2021-08-26 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0005_DATA_handle_existing_records'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packagebuild',
            name='epoch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='package_builds', to='packages.epoch'),
        ),
    ]
