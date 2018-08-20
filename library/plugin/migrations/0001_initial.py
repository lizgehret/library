# Generated by Django 2.1 on 2018-08-21 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plugin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=500, unique=True)),
                ('short_summary', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('install_guide', models.TextField()),
                ('published', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-updated_at'],
            },
        ),
    ]