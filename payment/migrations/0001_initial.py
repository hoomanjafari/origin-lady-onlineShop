# Generated by Django 5.0.2 on 2024-03-05 18:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0005_alter_allclothes_discount_percentage'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemOrdered',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_quantity', models.CharField(max_length=10)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_ordered_customer', to=settings.AUTH_USER_MODEL)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_ordered_product', to='shop.allclothes')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=33)),
                ('total_paid', models.CharField(max_length=33)),
                ('paid_time', models.DateTimeField(auto_now_add=True)),
                ('track_id', models.CharField(max_length=33)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
