# Generated by Django 2.1 on 2021-06-03 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vault', '0003_compliance_employee_compliance'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee_compliance',
            name='compl_ques_id',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]