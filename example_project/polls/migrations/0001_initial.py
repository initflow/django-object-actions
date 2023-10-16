# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-25 17:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Choice",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("choice_text", models.CharField(max_length=200)),
                ("votes", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "uuid",
                    models.UUIDField(editable=False, primary_key=True, serialize=False),
                ),
                ("comment", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Poll",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("question", models.CharField(max_length=200)),
                ("pub_date", models.DateTimeField(verbose_name=b"date published")),
            ],
        ),
        migrations.AddField(
            model_name="choice",
            name="poll",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="polls.Poll"
            ),
        ),
    ]
