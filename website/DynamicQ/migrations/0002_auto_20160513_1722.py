# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-13 11:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DynamicQ', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result_text', models.CharField(max_length=250)),
            ],
        ),
        migrations.AlterField(
            model_name='choice',
            name='choice_text',
            field=models.CharField(max_length=250),
        ),
        migrations.AddField(
            model_name='result',
            name='choice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DynamicQ.Choice'),
        ),
    ]
