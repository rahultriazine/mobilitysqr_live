# Generated by Django 2.2 on 2021-06-21 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vault', '0003_remove_vault_type_info_test'),
    ]

    operations = [
        migrations.RenameField(
            model_name='compliance',
            old_name='ques_id',
            new_name='question_id',
        ),
        migrations.RemoveField(
            model_name='employee_compliance',
            name='ques_id',
        ),
        migrations.AddField(
            model_name='employee_compliance',
            name='question_id',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]