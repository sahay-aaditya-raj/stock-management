# Generated by Django 4.2.4 on 2023-08-03 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_party_city_alter_party_addressline_2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='party',
            name='city',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
