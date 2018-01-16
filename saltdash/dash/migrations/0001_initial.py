# Generated by Django 2.0.1 on 2018-01-16 05:05

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobID',
            fields=[
                ('jid', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='job id')),
                ('load', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
            options={
                'db_table': 'jids',
                'ordering': ['-jid'],
            },
        ),
        migrations.CreateModel(
            name='SaltReturn',
            fields=[
                ('auto_id', models.AutoField(primary_key=True, serialize=False)),
                ('id', models.CharField(db_index=True, max_length=100, verbose_name='minion')),
                ('jid', models.CharField(db_index=True, max_length=50, verbose_name='job id')),
                ('fun', models.CharField(max_length=100, verbose_name='function')),
                ('fun_args', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), null=True, size=None, verbose_name='function args')),
                ('completed', models.DateTimeField(db_column='alter_time')),
                ('full_ret', django.contrib.postgres.fields.jsonb.JSONField(verbose_name='full result')),
                ('return_val', django.contrib.postgres.fields.jsonb.JSONField(db_column='return', verbose_name='result')),
                ('success', models.BooleanField()),
            ],
            options={
                'db_table': 'salt_returns',
                'ordering': ['-completed'],
            },
        ),
    ]
