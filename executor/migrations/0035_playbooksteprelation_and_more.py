# Generated by Django 4.1.13 on 2024-06-12 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userinvitation'),
        ('executor', '0034_playbookexecution_execution_global_variable_set'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayBookStepRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition', models.JSONField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.account')),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='child_step', to='executor.playbookstep')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parent_step', to='executor.playbookstep')),
                ('playbook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='executor.playbook')),
            ],
            options={
                'unique_together': {('account', 'playbook', 'parent', 'child')},
            },
        ),
        migrations.CreateModel(
            name='PlayBookStepRelationExecutionLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evaluation_result', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.account')),
                ('playbook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='executor.playbook')),
                ('playbook_execution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='executor.playbookexecution')),
                ('playbook_step_execution_log', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='executor.playbookstepexecutionlog')),
                ('playbook_step_relation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='executor.playbooksteprelation')),
            ],
        ),
    ]
