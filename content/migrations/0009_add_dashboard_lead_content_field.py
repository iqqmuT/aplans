# Generated by Django 2.2.9 on 2020-01-15 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0008_add_new_general_content_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitegeneralcontent',
            name='dashboard_lead_content',
            field=models.TextField(blank=True, verbose_name='dashboard lead content'),
        ),
    ]
