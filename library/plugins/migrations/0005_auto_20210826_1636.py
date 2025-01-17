# Generated by Django 3.2.6 on 2021-08-26 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plugins', '0004_deprecate_old_plugin_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='legacyplugin',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created At'),
        ),
        migrations.AlterField(
            model_name='legacyplugin',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated At'),
        ),
        migrations.AlterField(
            model_name='legacypluginauthorship',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created At'),
        ),
        migrations.AlterField(
            model_name='legacypluginauthorship',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated At'),
        ),
    ]
