# Generated by Django 5.0.6 on 2024-06-09 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_remove_course_student_student_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='cummulative',
            field=models.DecimalField(decimal_places=2, default=4.0, editable=False, max_digits=3),
        ),
    ]
