# Generated by Django 5.0.6 on 2024-06-09 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_lecturer_middle_name_alter_student_middle_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_code',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_title',
            field=models.CharField(max_length=256),
        ),
    ]
