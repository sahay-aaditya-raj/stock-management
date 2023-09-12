# Generated by Django 4.2.4 on 2023-09-01 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_party_mbno'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BonusAndGST',
        ),
        migrations.AddField(
            model_name='entry',
            name='bonus',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='invoice',
            name='gstrate',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='savedinvoice',
            name='mbno',
            field=models.CharField(default='', max_length=20),
        ),
    ]
