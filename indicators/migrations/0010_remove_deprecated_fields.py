# Generated by Django 2.1.5 on 2019-02-05 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('indicators', '0009_migrate_indicator_levels'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='indicator',
            name='level',
        ),
        migrations.RemoveField(
            model_name='indicator',
            name='plan',
        ),
    ]
