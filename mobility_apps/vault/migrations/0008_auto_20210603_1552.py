# Generated by Django 2.1 on 2021-06-03 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vault', '0007_auto_20210603_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compliance',
            name='ques_id',
            field=models.CharField(default='ques_id', max_length=200),
        ),
        migrations.AlterField(
            model_name='employee_compliance',
            name='ques_id',
            field=models.CharField(default='ques_id', max_length=200),
        ),
    ]