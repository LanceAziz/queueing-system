# Generated by Django 5.0.7 on 2024-08-24 02:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_client_client_teller_id_client_client_served'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Voice',
        ),
    ]
