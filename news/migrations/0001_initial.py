# Generated by Django 4.0.3 on 2022-03-04 17:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="News",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=500)),
                ("link", models.CharField(max_length=500)),
                ("creation_date", models.DateTimeField(auto_now_add=True)),
                ("no_of_votes", models.IntegerField()),
                ("author_name", models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("author", models.CharField(max_length=250)),
                ("content", models.TextField()),
                ("creation_date", models.DateTimeField(auto_now_add=True)),
                (
                    "news",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="news.news",
                    ),
                ),
            ],
        ),
    ]