# Generated by Django 3.2.4 on 2021-06-27 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0004_alter_materials_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='materials',
            name='image',
            field=models.ImageField(default=0, upload_to='images/'),
        ),
    ]
