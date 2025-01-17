# Generated by Django 3.2.7 on 2021-09-08 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0007_auto_20210903_1942'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='distrobuild',
            name='github_run_id',
        ),
        migrations.AddField(
            model_name='distrobuild',
            name='passed_github_run_id',
            field=models.CharField(default='', max_length=100, verbose_name='Passed GH Run ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='distrobuild',
            name='staged_github_run_id',
            field=models.CharField(default='', max_length=100, verbose_name='Staged GH Run ID'),
            preserve_default=False,
        ),
    ]
