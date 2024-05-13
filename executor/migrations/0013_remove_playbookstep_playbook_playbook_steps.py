# Generated by Django 4.1.13 on 2024-05-10 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('executor', '0012_populate_playbook_step_mapping'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playbookstep',
            name='playbook',
        ),
        migrations.AddField(
            model_name='playbook',
            name='steps',
            field=models.ManyToManyField(related_name='playbook_steps', through='executor.PlayBookStepMapping', to='executor.playbookstep'),
        ),
    ]