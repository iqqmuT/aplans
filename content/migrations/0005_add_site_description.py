# Generated by Django 2.2.4 on 2019-10-21 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_add_site_general_content_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitegeneralcontent',
            name='site_description',
            field=models.CharField(blank=True, max_length=150, verbose_name='site description'),
        ),
    ]