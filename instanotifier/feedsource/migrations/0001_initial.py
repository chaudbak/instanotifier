# Generated by Django 2.2.2 on 2019-06-20 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="FeedSource",
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
                ("url", models.URLField()),
                ("email_to", models.CharField(max_length=255)),
                ("enabled", models.BooleanField(default=True)),
            ],
        )
    ]