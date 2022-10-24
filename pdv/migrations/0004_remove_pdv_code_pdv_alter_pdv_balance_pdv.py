# Generated by Django 4.1.2 on 2022-10-24 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pdv", "0003_alter_pdv_active_pdv"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="pdv",
            name="code_pdv",
        ),
        migrations.AlterField(
            model_name="pdv",
            name="balance_pdv",
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
    ]
