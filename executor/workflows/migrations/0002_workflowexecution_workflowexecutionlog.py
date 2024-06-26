# Generated by Django 4.1.4 on 2024-04-23 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userinvitation'),
        ('executor', '0003_playbookexecution_time_range_and_more'),
        ('workflows', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkflowExecution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workflow_run_id', models.CharField(db_index=True, max_length=256)),
                ('status', models.IntegerField(choices=[(0, 'UNKNOWN_WORKFLOW_STATUS'), (1, 'WORKFLOW_SCHEDULED'), (2, 'WORKFLOW_RUNNING'), (3, 'WORKFLOW_FINISHED'), (4, 'WORKFLOW_FAILED'), (5, 'WORKFLOW_CANCELLED')], db_index=True, default=1)),
                ('scheduled_at', models.DateTimeField(db_index=True)),
                ('expiry_at', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('interval', models.IntegerField(db_index=True, default=60)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('started_at', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('finished_at', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('time_range', models.JSONField(blank=True, null=True)),
                ('created_by', models.TextField(blank=True, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.account')),
                ('workflow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workflows.workflow')),
            ],
            options={
                'unique_together': {('account', 'workflow_run_id')},
            },
        ),
        migrations.CreateModel(
            name='WorkflowExecutionLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.account')),
                ('playbook_execution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='executor.playbookexecution')),
                ('workflow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workflows.workflow')),
                ('workflow_execution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workflows.workflowexecution')),
            ],
        ),
    ]
