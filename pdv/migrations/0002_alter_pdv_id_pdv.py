# Generated by Django 4.1.2 on 2022-10-23 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pdv", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pdv",
            name="id_pdv",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
