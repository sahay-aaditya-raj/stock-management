# Generated by Django 4.2.4 on 2023-08-04 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_manufacturers_alias'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='invoicenumber',
            field=models.CharField(max_length=10),
        ),
    ]
