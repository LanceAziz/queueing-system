# Generated by Django 5.0.7 on 2024-08-09 21:01

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_client_client_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='client_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
