# Generated by Django 4.1.13 on 2024-06-11 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('executor', '0033_playbookstepexecutionlog_created_by_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='playbookexecution',
            name='execution_global_variable_set',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
