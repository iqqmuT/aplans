# Generated by Django 2.1.3 on 2019-01-15 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actions', '0010_remove_indicators_new'),
    ]

    operations = [
        migrations.RenameField(
            model_name='action',
            old_name='indicators_new',
            new_name='indicators',
        ),
    ]
