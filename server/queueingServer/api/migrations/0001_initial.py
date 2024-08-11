# Generated by Django 5.0.7 on 2024-08-09 20:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teller',
            fields=[
                ('teller_id', models.AutoField(primary_key=True, serialize=False)),
                ('teller_num', models.IntegerField()),
                ('teller_type', models.CharField(max_length=45)),
                ('teller_pass', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Voice',
            fields=[
                ('voice_id', models.AutoField(primary_key=True, serialize=False)),
                ('voice_name', models.CharField(max_length=45)),
                ('voice_file', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('client_id', models.AutoField(primary_key=True, serialize=False)),
                ('client_num', models.IntegerField()),
                ('client_date', models.DateTimeField()),
                ('client_type', models.CharField(max_length=45)),
                ('client_teller_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.teller')),
            ],
        ),
    ]
