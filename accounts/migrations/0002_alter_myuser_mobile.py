# Generated by Django 5.0.2 on 2024-02-12 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='mobile',
            field=models.PositiveIntegerField(unique=True),
        ),
    ]