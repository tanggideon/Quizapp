# Generated by Django 5.0.6 on 2024-06-16 17:14

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_alter_lecturer_position'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.course')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]