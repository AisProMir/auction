# Generated by Django 4.2.6 on 2023-12-21 16:57

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0002_alter_transport_name"),
    ]

    operations = [
        migrations.RenameField(
            model_name="informationofcargo",
            old_name="Obiom",
            new_name="obiom",
        ),
        migrations.RenameField(
            model_name="informationofcargo",
            old_name="Ves",
            new_name="ves",
        ),
    ]
