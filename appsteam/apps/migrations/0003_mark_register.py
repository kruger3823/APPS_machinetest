# Generated by Django 4.1 on 2022-08-09 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("apps", "0002_mark_delete_covidcase_delete_covidoutbreaks_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="mark",
            name="register",
            field=models.CharField(max_length=200, null=True),
        ),
    ]
