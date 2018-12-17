# Generated by Django 2.1.3 on 2018-12-17 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actions', '0005_add_decision_level_and_contact_persons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='description',
            field=models.TextField(blank=True, help_text='What does this action involve in more detail?', null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='action',
            name='official_name',
            field=models.TextField(blank=True, help_text='The name as approved by an official party', null=True, verbose_name='official name'),
        ),
        migrations.AlterField(
            model_name='actiontask',
            name='state',
            field=models.CharField(choices=[('active', 'active'), ('cancelled', 'cancelled')], default='active', max_length=20, verbose_name='state'),
        ),
    ]