# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-30 07:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160702_0830'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_author', models.CharField(max_length=150)),
                ('comment_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('comment_body', models.TextField(blank=True, null=True)),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Page')),
            ],
        ),
    ]
