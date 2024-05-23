# Generated by Django 4.1.13 on 2024-05-16 07:29

from django.db import migrations

from executor.utils.old_to_new_model_transformers import \
    transform_PlaybookTaskExecutionResult_json_to_PlaybookTaskResult_json


def port_playbook_task_execution_logs_to_new_protos(apps, schema_editor):
    PlayBookTaskExecutionLog = apps.get_model("executor", "PlayBookTaskExecutionLog")

    for ptlg in PlayBookTaskExecutionLog.objects.all():
        old_task_result = ptlg.playbook_task_result
        try:
            new_task_result = transform_PlaybookTaskExecutionResult_json_to_PlaybookTaskResult_json(old_task_result)
            ptlg.playbook_task_result = new_task_result
            ptlg.save(update_fields=["playbook_task_result"])
        except Exception as e:
            print(f"Error transforming PlaybookTaskExecutionResult: {e}")
            continue


class Migration(migrations.Migration):
    dependencies = [
        ('executor', '0023_rename_playbooktaskdefinition_playbooktask'),
    ]

    operations = [
        migrations.RunPython(port_playbook_task_execution_logs_to_new_protos, migrations.RunPython.noop)
    ]
