# Generated by Django 4.2.4 on 2023-08-24 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_saveentries_pack'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saveentries',
            name='pts',
            field=models.CharField(default=None, max_length=8),
        ),
    ]
