# Generated by Django 4.1.4 on 2024-05-07 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userinvitation'),
        ('executor', '0005_playbookstep_interpreter_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='playbookexecutionlog',
            name='interpretation',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='PlayBookStepExecutionLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interpretation', models.JSONField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.account')),
                ('playbook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='executor.playbook')),
                ('playbook_execution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='executor.playbookexecution')),
                ('playbook_step', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='executor.playbookstep')),
            ],
        ),
        migrations.AddField(
            model_name='playbookexecutionlog',
            name='playbook_step_execution_log',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='executor.playbookstepexecutionlog'),
        ),
    ]