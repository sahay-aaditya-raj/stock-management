# Generated by Django 4.2.4 on 2023-08-03 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manufacturers',
            name='alias',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='manufacturers',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='products',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='products',
            name='volume',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='stock',
            name='batch',
            field=models.CharField(max_length=20),
        ),
    ]
