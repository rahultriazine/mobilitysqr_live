# Generated by Django 2.1.15 on 2021-03-25 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vault', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vault_type_info',
            name='test',
        ),
    ]