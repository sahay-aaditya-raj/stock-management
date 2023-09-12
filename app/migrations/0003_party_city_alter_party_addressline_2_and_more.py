# Generated by Django 4.2.4 on 2023-08-03 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_manufacturers_alias_alter_manufacturers_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='party',
            name='city',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='party',
            name='addressLine_2',
            field=models.TextField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='party',
            name='addressLine_3',
            field=models.TextField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='party',
            name='dlno',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='party',
            name='gstid',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='party',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]