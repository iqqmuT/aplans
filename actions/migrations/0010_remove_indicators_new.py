# Generated by Django 2.1.3 on 2019-01-15 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actions', '0009_migrate_indicators'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='action',
            name='indicators',
        ),
    ]
