# Generated by Django 2.1 on 2021-07-12 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0002_auto_20210712_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor_income',
            name='column13',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
