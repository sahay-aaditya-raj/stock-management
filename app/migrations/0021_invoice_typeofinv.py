# Generated by Django 4.2.4 on 2023-09-01 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_delete_bonusandgst_entry_bonus_invoice_gstrate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='typeofinv',
            field=models.BooleanField(default=False),
        ),
    ]
