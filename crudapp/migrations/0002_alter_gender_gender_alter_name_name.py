# Generated by Django 4.0.5 on 2022-06-06 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gender',
            name='gender',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='name',
            name='name',
            field=models.CharField(max_length=256),
        ),
    ]