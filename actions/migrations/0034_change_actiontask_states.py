# Generated by Django 2.2.6 on 2019-11-29 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actions', '0033_add_field_allow_images_for_actions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actiontask',
            name='completed_at',
            field=models.DateField(blank=True, help_text='The date when the task was completed', null=True, verbose_name='completion date'),
        ),
        migrations.AlterField(
            model_name='actiontask',
            name='due_at',
            field=models.DateField(help_text='The date by which the task should be completed (deadline)', verbose_name='due date'),
        ),
        migrations.AlterField(
            model_name='actiontask',
            name='state',
            field=models.CharField(choices=[('not_started', 'not started'), ('in_progress', 'in progress'), ('completed', 'completed'), ('cancelled', 'cancelled')], default='not_started', max_length=20, verbose_name='state'),
        ),
    ]