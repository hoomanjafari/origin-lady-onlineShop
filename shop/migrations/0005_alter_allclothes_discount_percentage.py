# Generated by Django 5.0.2 on 2024-03-03 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_allclothes_discount_allclothes_discount_percentage_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allclothes',
            name='discount_percentage',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=6, null=True),
        ),
    ]
