# Generated by Django 5.0.6 on 2024-06-10 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_remove_lecturer_course_course_lecturer'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(related_name='coursestudents', to='home.student'),
        ),
    ]