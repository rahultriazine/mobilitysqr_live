# Generated by Django 2.1.15 on 2021-03-05 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_auto_20210226_1642'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calender_Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_name', models.CharField(blank=True, max_length=100, null=True)),
                ('activity_sort_name', models.CharField(blank=True, max_length=100, null=True)),
                ('is_visible', models.CharField(default=True, max_length=50)),
                ('column1', models.CharField(blank=True, max_length=100, null=True)),
                ('column2', models.CharField(blank=True, max_length=100, null=True)),
                ('column3', models.CharField(blank=True, max_length=100, null=True)),
                ('column4', models.CharField(blank=True, max_length=100, null=True)),
                ('column5', models.CharField(blank=True, max_length=100, null=True)),
                ('column6', models.CharField(blank=True, max_length=100, null=True)),
                ('column7', models.CharField(blank=True, max_length=100, null=True)),
                ('column8', models.CharField(blank=True, max_length=100, null=True)),
                ('column9', models.CharField(blank=True, max_length=100, null=True)),
                ('column10', models.CharField(blank=True, max_length=100, null=True)),
                ('column11', models.CharField(blank=True, max_length=100, null=True)),
                ('column12', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Calender Activity',
                'verbose_name_plural': 'Calender Activity',
                'managed': True,
            },
        ),
    ]