# Generated by Django 4.1.4 on 2024-04-25 07:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("workflows", "0005_alter_workflowexecution_interval"),
    ]

    operations = [
        migrations.AddField(
            model_name="workflowexecution",
            name="metadata",
            field=models.JSONField(blank=True, null=True),
        ),
    ]