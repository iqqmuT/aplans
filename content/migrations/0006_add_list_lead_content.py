# Generated by Django 2.2.4 on 2019-10-22 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_add_site_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sitegeneralcontent',
            options={'verbose_name': 'site general content', 'verbose_name_plural': 'site general contents'},
        ),
        migrations.AddField(
            model_name='sitegeneralcontent',
            name='action_list_lead_content',
            field=models.TextField(blank=True, verbose_name='action list lead content'),
        ),
        migrations.AddField(
            model_name='sitegeneralcontent',
            name='indicator_list_lead_content',
            field=models.TextField(blank=True, verbose_name='indicator list lead content'),
        ),
        migrations.AlterField(
            model_name='sitegeneralcontent',
            name='hero_content',
            field=models.TextField(blank=True, verbose_name='hero content'),
        ),
    ]
