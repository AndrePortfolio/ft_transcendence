# Generated by Django 5.2 on 2025-04-23 09:41

import django.contrib.postgres.fields
import django.contrib.postgres.fields.hstore
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tournament_id', models.CharField(max_length=100, unique=True)),
                ('max_players', models.IntegerField(default=4)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('winner', models.CharField(max_length=150, null=True)),
                ('winner_id', models.CharField(max_length=150, null=True)),
                ('players', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=150), default=list, size=None)),
                ('player_ids', django.contrib.postgres.fields.hstore.HStoreField()),
                ('rounds', models.JSONField(default=list)),
                ('current_round', models.IntegerField(default=0)),
                ('current_round_created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('REGISTERING', 'Registering'), ('IN_PROGRESS', 'In Progress'), ('COMPLETED', 'Completed')], default='REGISTERING', max_length=20)),
            ],
        ),
    ]
