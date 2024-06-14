# Generated by Django 4.1.13 on 2024-06-11 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflows', '0008_migrate_old_to_new_def'),
    ]

    operations = [
        migrations.AddField(
            model_name='workflow',
            name='configuration',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='workflowexecution',
            name='workflow_execution_configuration',
            field=models.JSONField(blank=True, null=True),
        ),
    ]