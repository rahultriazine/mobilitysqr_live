# Generated by Django 2.2 on 2021-06-16 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location_master',
            name='location_code',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]