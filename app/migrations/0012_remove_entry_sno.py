# Generated by Django 4.2.4 on 2023-08-22 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_entry_qty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='sno',
        ),
    ]
