# Generated by Django 4.1.6 on 2023-02-07 15:28

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("teams", "0003_rename_titles_team_tittles"),
    ]

    operations = [
        migrations.RenameField(
            model_name="team",
            old_name="tittles",
            new_name="titles",
        ),
    ]
