# Generated by Django 2.1 on 2021-06-03 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vault', '0008_auto_20210603_1552'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compliance',
            name='ques_id',
        ),
        migrations.RemoveField(
            model_name='employee_compliance',
            name='ques_id',
        ),
        migrations.AddField(
            model_name='compliance',
            name='ques_id_compl',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='employee_compliance',
            name='ques_id_compl',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]