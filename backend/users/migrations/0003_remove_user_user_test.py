# Generated by Django 2.2.26 on 2022-01-24 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_auto_20220124_1621"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="user_test",
        ),
    ]
