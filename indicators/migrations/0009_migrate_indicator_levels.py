# Generated by Django 2.1.5 on 2019-02-05 08:57

from django.db import migrations


def migrate_indicator_levels(apps, schema_editor):
    Indicator = apps.get_model('indicators', 'Indicator')
    IndicatorLevel = apps.get_model('indicators', 'IndicatorLevel')

    for indicator in Indicator.objects.all():
        IndicatorLevel.objects.create(indicator=indicator, plan=indicator.plan, level=indicator.level)


class Migration(migrations.Migration):
    dependencies = [
        ('indicators', '0008_add_indicator_level_relation'),
    ]

    operations = [
        migrations.RunPython(migrate_indicator_levels)
    ]
