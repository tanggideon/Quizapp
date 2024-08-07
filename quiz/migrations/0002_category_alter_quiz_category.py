# Generated by Django 5.0.6 on 2024-07-27 00:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=32)),
                ('require_qrcode', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='quiz',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='quiz.category'),
        ),
    ]
